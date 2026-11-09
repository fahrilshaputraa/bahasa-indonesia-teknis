# Dokumen uji (UAT, TRF)

Pembaca utamanya penguji non-teknis. Tiap kolom harus bisa dikerjakan atau dinilai tanpa bertanya.

## Judul

Nama menu atau halaman di depan, lalu kejadian yang bisa dilihat penguji. Batasi sekitar 90 karakter dan satu gagasan utama; bila ada dua hal, pilih yang menentukan lulus atau gagal dan pindahkan sisanya ke deskripsi. Tulis apa yang ditolak atau tampil, bukan konsep keamanan.

| Sebelum | Sesudah |
|---|---|
| Login: Pengguna Tanpa Akses Ditolak dan Identitas Tidak Bisa Dipalsukan | Halaman Admin: Tanpa Akses Ditolak, Meminta Data "sebagai Admin" Tidak Menambah Akses |
| Filter Data Disaring Sesuai Izin Baca | Laporan: Data yang Tidak Boleh Dilihat Tidak Ditampilkan |

## Prasyarat

Satu kalimat: akun, data, dan kondisi yang harus siap. Siapa yang mengerjakan langkah tertentu dan alat khusus yang diperlukan ditulis di sini.

- Sebelum (di langkah): `Kirim request langsung ke alamat berikut (dikerjakan tim teknis, perlu alat khusus): …`
- Sesudah (prasyarat): `Siapkan akun tanpa izin ekspor. Langkah 2 dikerjakan tim teknis karena perlu alat untuk mengirim request.`

## Langkah

Satu langkah satu aksi, diawali kata kerja perintah: Buka, Klik, Isi, Pilih, Periksa. Sebut nilai yang harus diisi. Untuk request, sebut metode dan alamat persisnya. Keterangan dalam kurung tentang siapa atau alat tidak masuk ke langkah.

| Sebelum | Sesudah |
|---|---|
| Lakukan pengecekan pada halaman laporan | Buka halaman Laporan dan periksa kolom Total |
| Kirim langsung ke alamat API berikut (dikerjakan tim teknis): POST /api/orders/export | Kirim request POST langsung ke /api/orders/export |

## Hasil yang diharapkan

Kalimat pernyataan yang bisa dinilai Lolos atau Gagal tanpa menafsirkan. Sebut pembandingnya. Hindari "benar", "baik", dan "sesuai" tanpa pembanding.

| Sebelum | Sesudah |
|---|---|
| Tampilan sesuai dan benar | Total pesanan sama dengan jumlah baris pada tab Pesanan |
| Request ditolak | Request ditolak dengan kode 403 dan data tidak berubah |

## Penomoran

Nomor hasil sama dengan nomor langkahnya, supaya hasil yang gagal bisa ditelusuri ke langkahnya.

## Satu butir uji, satu tujuan

Bila satu bagian gagal dan Kesimpulan tidak bisa menunjukkan bagian mana, pecah butir uji itu. Tanda butir yang terlalu besar: banyak langkah dari beberapa halaman berbeda, atau judul yang memuat tiga kata "dan".
