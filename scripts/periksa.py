#!/usr/bin/env python3
"""Pemeriksa teks Indonesia: menandai pola yang perlu dinilai, tidak mengubah berkas.

Pemakaian:
    python scripts/periksa.py berkas.md [berkas2.txt ...]
    cat teks.txt | python scripts/periksa.py -

Keluaran: berkas:baris: [KODE] pesan -> saran. Kode keluar 1 bila ada temuan.
Temuan adalah petunjuk, bukan vonis: nilai tiap temuan sebelum mengubah teks.
Hanya memakai pustaka standar.
"""
import re
import sys

# (kode, pola, pesan, saran)
ATURAN = [
    ("KK-01", r"\bmelakukan (pe\w+an|pen\w+an|peng\w+an)\b", "kalimat kaku (melakukan + kata benda)", "pakai kata kerja langsung, mis. 'mengecek'"),
    ("KK-02", r"\bterdapat\b", "kalimat kaku", "ada"),
    ("KK-03", r"\bpada saat ini\b", "kalimat kaku", "sekarang"),
    ("KK-04", r"\bdalam rangka untuk\b", "kalimat kaku", "untuk"),
    ("KK-05", r"\bhal ini dikarenakan\b", "kalimat kaku", "ini terjadi karena"),
    ("KK-06", r"\byang mana\b", "terjemahan harfiah 'which'", "yang, tempat, atau ketika"),
    ("KK-07", r"\bdapat dilakukan dengan cara\b", "kalimat kaku", "caranya"),
    ("EJ-01", r"\b(analisa|silahkan|nampak|ijin|resiko|aktifitas|praktek)\b", "bentuk tidak baku", "analisis, silakan, tampak, izin, risiko, aktivitas, praktik"),
    ("EJ-02", r"\b(merubah|dirubah)\b", "bentuk tidak baku", "mengubah, diubah"),
    ("EJ-03", r"\b(dimana|diantara)\b", "pemisahan kata depan", "di mana, di antara"),
    ("IS-01", r"\bkartu\b(?! (kredit|debit|nama|identitas|pos|ucapan|atm))", "kata 'kartu' ambigu untuk elemen antarmuka", "card (ikuti istilah.md)"),
    ("IS-02", r"\b(dipalsukan|ditiru)\b", "istilah abstrak untuk penguji non-teknis", "tulis kejadiannya, mis. 'tidak bisa menyamar sebagai pengguna lain'"),
    ("IS-03", r"\b(disaring|tersamarkan)\b", "kata sulit", "dibatasi / tidak ditampilkan / ditutupi"),
    ("IS-04", r"\bmenembak endpoint\b", "jargon", "mengirim request langsung ke alamat API"),
    ("PE-01", r"\b(silakan|mohon)\b", "kata pengisi pada prosedur", "perintah langsung, mis. 'Klik Simpan'"),
    ("PE-02", r"\b(mudah|cukup tinggal|hanya tinggal|dengan cepat)\b", "meremehkan pembaca", "hapus"),
    ("PE-03", r"!", "tanda seru", "titik"),
    ("LG-01", r"\((?:[^)]*\b(tim teknis|alat khusus|dikerjakan|dijalankan oleh)\b[^)]*)\)", "keterangan siapa/alat di dalam kurung", "pindahkan ke prasyarat"),
]


def kalimat_panjang(baris):
    for k in re.split(r"(?<=[.;?])\s+", baris):
        n = len(k.split())
        if n > 40:
            yield n


def periksa(nama, teks):
    temuan = 0
    for no, baris in enumerate(teks.splitlines(), 1):
        if baris.lstrip().startswith(("```", "    ")) or re.fullmatch(r"\s*`[^`]*`\s*", baris):
            continue
        # kutipan dan kode inline tidak diperiksa
        bersih = re.sub(r"`[^`]*`|\"[^\"]*\"", " ", baris)
        for kode, pola, pesan, saran in ATURAN:
            if re.search(pola, bersih, flags=re.IGNORECASE):
                print(f"{nama}:{no}: [{kode}] {pesan} -> {saran}")
                temuan += 1
        for n in kalimat_panjang(bersih):
            print(f"{nama}:{no}: [KL-01] kalimat {n} kata -> pecah (sekitar 25 kata)")
            temuan += 1
    return temuan


def main(argumen):
    if not argumen:
        print(__doc__)
        return 2
    total = 0
    for a in argumen:
        if a == "-":
            total += periksa("<stdin>", sys.stdin.read())
        else:
            with open(a, encoding="utf-8") as f:
                total += periksa(a, f.read())
    print(f"{total} temuan")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
