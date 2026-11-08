# Paket Self-check Praktikum Perulangan / Loop Practicum Self-check

## Bahasa Indonesia

`selfcheck.py` memeriksa kode praktikum secara otomatis. Hasilnya membantu menemukan kesalahan, tetapi bukan nilai akhir. Program ini hanya memakai pustaka standar Python 3.8 atau lebih baru.

### Cara memakai

1. Salin `selfcheck.py` ke folder utama repositori, sejajar dengan folder `blok1` dan `studi_kasus`.
2. Buka terminal di folder utama repositori.
3. Jalankan salah satu perintah berikut. Jika `python` tidak dikenali, gunakan `python3` atau `py`.

```text
python selfcheck.py --digit 7              periksa semua tugas
python selfcheck.py --digit 7 --target 2   periksa studi kasus sampai target 2
python selfcheck.py --task t14             periksa satu tugas
python selfcheck.py --digit 7 --task score periksa studi kasus saja
```

Ganti angka 7 dengan digit terakhir NIM Anda.

### Membaca hasil

| Status | Arti |
|---|---|
| LULUS | Semua pemeriksaan otomatis terpenuhi |
| GAGAL | Ada output, struktur kode, atau batasan modul yang belum sesuai |
| BELUM ADA | File tugas wajib tidak ditemukan |
| DILEWATI | File tantangan opsional tidak ada |

Spasi di akhir baris dan teks prompt `input()` tidak dinilai. Program yang berjalan lebih dari 3 detik dianggap tidak berhenti.

### Cakupan

Semua tugas kode wajib, tantangan opsional, dan studi kasus diperiksa. Tracing, bug log, pseudocode, tabel uji, kerapian kode, dan pemahaman tidak diperiksa. `p1_stop_loop.py` tidak diperiksa karena memang dibuat tidak berhenti.

## English

`selfcheck.py` checks the practicum code automatically. The result helps you find mistakes, but it is not your final grade. It uses only the standard library of Python 3.8 or later.

### How to use

1. Copy `selfcheck.py` to the repository root, next to the `blok1` and `studi_kasus` folders.
2. Open a terminal in the repository root.
3. Run one of these commands. If `python` is not recognized, use `python3` or `py`.

```text
python selfcheck.py --lang en --digit 7              check all tasks
python selfcheck.py --lang en --digit 7 --target 2   check the case study up to target 2
python selfcheck.py --lang en --task t14             check one task
python selfcheck.py --lang en --digit 7 --task score check only the case study
```

Replace 7 with the last digit of your student ID.

### Reading the result

| Status | Meaning |
|---|---|
| PASS | All automatic checks were met |
| FAIL | The output, code structure, or a module restriction needs attention |
| MISSING | A required task file was not found |
| SKIPPED | An optional challenge file does not exist |

Trailing spaces and `input()` prompt text are not assessed. A program that runs longer than 3 seconds is treated as not stopping.

### Coverage

All required code tasks, optional challenges, and the case study are checked. Tracing, bug logs, pseudocode, test tables, code style, and understanding are not checked. `p1_stop_loop.py` is not checked because it is designed not to stop.
