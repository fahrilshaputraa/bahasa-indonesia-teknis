# bahasa-indonesia-teknis

Skill untuk agent coding (Claude Code, Codex, dan sejenisnya) agar menulis dan menyunting teks berbahasa Indonesia yang jelas dibaca orang non-teknis: dokumen uji, proposal, laporan, panduan, teks antarmuka, dan pesan error.

## Isi
- `SKILL.md`: kontrak, batas perubahan, alur, dan peta masalah.
- `references/`: istilah, kalimat, dokumen uji, proposal dan laporan, antarmuka dan error. Dimuat hanya saat masalahnya muncul.
- `scripts/periksa.py`: pemeriksa pola (pustaka standar Python). `python scripts/periksa.py berkas.md`
- `evals/cases.json`: kasus uji untuk membandingkan hasil dengan dan tanpa skill.

## Pemasangan
Salin folder ini ke direktori skill agent Anda, misalnya `~/.claude/skills/bahasa-indonesia-teknis`.

## Lisensi
MIT. Bebas dipakai, disalin, dan diubah; lihat berkas `LICENSE`.
