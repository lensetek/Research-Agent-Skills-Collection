---
name: paper-matrix-builder
description: >-
  Membuat matriks perbandingan paper terstruktur, tabel ekstraksi data Systematic Literature Review (SLR), dan peta bukti (evidence map) secara otomatis dan konsisten.
---

# Paper Matrix Builder

## Overview
Skill ini ditujukan untuk mengotomatiskan pembuatan matriks penelitian terdahulu (*State-of-the-Art matrix*) secara sistematis. Dengan menyusun data teknis seperti metode, dataset, metrik pengujian, dan hasil performa ke dalam satu tabel yang terstandarisasi, peneliti dapat dengan mudah memetakan posisi riset mereka di antara riset sejenis.

## Dependencies
- `extract-methodology`

## Quick Start
Contoh penggunaan:
*"Gunakan skill paper-matrix-builder untuk menyusun tabel matriks perbandingan metodologi dari 5 paper terpilih tentang klasifikasi fraud detection."*

## Workflow

### 1. Penentuan Dimensi Pembanding (Matrix Schema Selection)
Pilih schema matriks berdasarkan kebutuhan analisis:
- **Matriks Metodologi (Teknis)**: Membandingkan arsitektur model, parameter, hyperparameter, dan lingkungan eksperimen.
- **Matriks Data & Evaluasi**: Membandingkan tipe dataset, ukuran data, metrik pengujian, dan performa numerik.
- **Matriks Kajian Literatur (SLR)**: Membandingkan fokus studi, gap, kontribusi, keterbatasan, dan relevansi.

### 2. Ekstraksi Data Konsisten
- Gunakan data yang telah diekstrak secara akurat (melalui skill `extract-methodology`).
- Pastikan tidak ada data yang dikarang. Jika informasi dari suatu paper tidak lengkap, wajib diisi dengan **"tidak dilaporkan"** atau **"tidak disebutkan"**.

### 3. Pembuatan Tabel Komparasi (Programmatic Matrix Generation)
- **Eksekusi Helper Programatik (WAJIB)**: Sebelum menyusun rincian narasi, jalankan skrip pembangun matriks untuk mengombinasikan JSON ekstraksi menjadi tabel Markdown dan CSV yang terstandarisasi *(Gunakan path absolut dari `build_sota_matrix.py` di direktori instalasi skill ini)*:
  ```bash
  python "<PATH_KE_SKILL>/scripts/build_sota_matrix.py" --input extractions/ --output-md sota_matrix.md --output-csv sota_matrix.csv
  ```
- Tampilkan isi `sota_matrix.md` ke dalam jawaban akhir agen. Format tabel standar:
| Penulis & Tahun | Pendekatan/Model | Dataset Utama | Parameter Kunci | Metrik Evaluasi | Angka Performa | Celah / Keterbatasan |
|---|---|---|---|---|---|---|

### 4. Pembuatan Evidence Map (Peta Bukti / Taksonomi)
Grup-kan paper berdasarkan kluster tertentu (misalnya kluster metode, kluster dataset, atau kluster tahun publikasi) untuk menunjukkan konsentrasi arah riset dan area kosong (*white spaces*) yang belum banyak disentuh.

## Common Mistakes & Aturan Kritis
- **Halusinasi & Pemalsuan Data (FATAL)**: Dilarang keras mengarang atau menebak data teknis, metode, atau arsitektur dari sebuah paper untuk mengisi kekosongan tabel. Anda wajib menuliskan "TIDAK DILAPORKAN" (Not Reported) jika informasi tersebut tidak ada di dalam paper asli.
- **Ketidakkonsistenan Format Kolom**: Mengubah susunan kolom di tengah matriks sehingga menyulitkan pembandingan langsung.
- **Membandingkan Metrik yang Tidak Kompatibel**: Memasukkan performa yang menggunakan metode validasi yang berbeda (misalnya membandingkan F1-score pengujian silang 10-fold dengan pengujian split data acak sederhana tanpa penjelasan).
- **Matriks yang Terlalu Padat Paragraf**: Memasukkan terlalu banyak teks narasi panjang di dalam sel tabel. Sel tabel matriks harus berisi poin-poin ringkas, parameter angka, atau frasa singkat.
- **Data Kosong yang Disembunyikan**: Menghapus baris atau kolom hanya karena suatu paper tidak melaporkan data tertentu. Tuliskan ketidaktersediaan data tersebut secara jujur karena itu merupakan bagian dari temuan keterbatasan paper tersebut.
