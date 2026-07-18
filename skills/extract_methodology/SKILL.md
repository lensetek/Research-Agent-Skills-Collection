---
name: extract-methodology
description: >-
  Membedah paper untuk mengekstrak detail teknis seperti metodologi, arsitektur model, parameter eksperimen, dataset, dan metrik kinerja secara presisi.
---

# Extract Methodology

## Overview
Skill ini ditujukan untuk membedah karya ilmiah secara mendalam guna menarik informasi metodologi eksperimen, alur algoritma/sistem, dataset yang digunakan, hyperparameter, dan hasil pengujian performa secara terstruktur dengan tingkat akurasi 100%. Ini sangat berguna ketika peneliti ingin mereproduksi (reproduce) penelitian terdahulu atau membandingkan baseline.

## Dependencies
- `literature-search-openalex`
- `literature-search-arxiv`
- `pubmed-database`

## Quick Start
Contoh penggunaan:
*"Gunakan skill extract-methodology untuk mengekstrak arsitektur model, dataset, dan hyperparameter dari paper GPT-3."*

## Workflow

### 1. Penentuan Target Ekstraksi
- Tentukan elemen teknis apa saja yang ingin diekstrak (e.g., nama model, dataset, metrik F1-score/Accuracy, optimizer, learning rate, hardware yang digunakan).

### 2. Pengambilan & Pre-parsing Paper (Mandatory Section Filtering)
- Cari ID paper atau URL paper menggunakan tools pencarian literatur.
- **Eksekusi Helper Programatik (WAJIB)**: Sebelum melakukan ekstraksi manual, jalankan skrip parser seksi untuk memfilter bagian Metode, Setup, dan Hasil guna mencegah *context overload* pada LLM *(Gunakan path absolut dari `parse_sections.py` di direktori instalasi skill ini)*:
  ```bash
  python "<PATH_KE_SKILL>/scripts/parse_sections.py" --input paper_text.md --output sections.json
  ```
- Evaluasi potongan seksi dari `sections.json` secara mendalam. Jangan berasumsi hanya dari abstrak.

### 3. Ekstraksi Informasi Terstruktur (10 Komponen Wajib)
Ekstrak informasi secara presisi ke dalam tabel Markdown atau skema JSON yang mencakup komponen berikut:
1. **Tujuan Paper**: Masalah spesifik yang ingin diselesaikan oleh penulis.
2. **Dataset**: Nama dataset, ukuran, sumber, label, periode data, pembagian train/val/test, dan teknik augmentasi data (jika ada).
3. **Preprocessing**: Langkah-langkah pembersihan, normalisasi, tokenisasi, atau ekstraksi fitur.
4. **Model/Metode**: Algoritma utama yang digunakan serta baseline yang dibandingkan.
5. **Arsitektur**: Detail arsitektur model, struktur jaringan, fungsi aktivasi, jumlah parameter, atau diagram alur sistem.
6. **Parameter**: Detail hyperparameter, learning rate, optimizer (e.g., AdamW), batch size, epoch, loss function, dan environment perangkat keras/lunak.
7. **Evaluasi**: Metrik pengujian (e.g., Accuracy, F1-Score, RMSE), skenario uji, validasi silang (cross-validation).
8. **Hasil Utama**: Angka performa model yang secara eksplisit dilaporkan dalam tabel/teks hasil eksperimen paper.
9. **Keterbatasan**: Hambatan/batasan yang diakui oleh penulis atau keterbatasan metodologi yang ditemukan agen secara kritis.
10. **Reproducibility**: Status ketersediaan repositori kode sumber (link GitHub/GitLab), petunjuk instalasi, dan aksesibilitas dataset (publik vs privat).

### 4. Analisis Reproduksibilitas (Reproducibility Check)
- Evaluasi apakah paper tersebut menyediakan informasi yang cukup untuk diimplementasikan ulang (reproduced).

### 5. Pelaporan Hasil Ekstraksi
- Buat rangkuman teknis yang bersih dan to-the-point menggunakan poin-poin terstruktur dan tabel data. Hindari narasi panjang lebar yang tidak perlu.

## Few-Shot Guidance (Contoh Benar vs Salah)

### ❌ [SALAH] Ekstraksi Mengambang / Mengarang
> **Learning Rate**: Umummnya 0.001 menggunakan Adam.  
> **Dataset Size**: Tidak disebutkan tetapi terlihat besar.

### ✅ [BENAR] Ekstraksi Faktual & Presisi
> **Learning Rate**: tidak dilaporkan  
> **Dataset Size**: 50,000 sampel transaksi (Tabel 1, Halaman 4)

## Common Mistakes & Aturan Kritis (Anti-Halusinasi)
- **Hanya Membaca Abstrak**: Abstrak jarang memuat detail teknis. Agen wajib menelusuri isi utama paper.
- **Klaim Tanpa Bukti & Halusinasi Parameter (FATAL)**: Dilarang keras mengarang nilai teknis!
  - Jika suatu hyperparameter tidak disebutkan di paper, wajib menuliskan **"tidak dilaporkan"** (jangan mengarang nilai atau menggunakan nilai default umum).
  - Jika dataset tidak jelas, wajib menuliskan **"tidak dijelaskan secara eksplisit"**.
  - Jika hasil performa disajikan dalam bentuk grafik tanpa angka tabel yang jelas, wajib menuliskan bahwa nilai tersebut ditaksir secara visual dari grafik dan sebutkan estimasi rentangnya.
- **Perbandingan Apel-ke-Jeruk (False Equivalence)**: Dilarang menyamakan atau membandingkan langsung performa antar-paper jika dataset, konfigurasi eksperimen, atau skenario pengujiannya berbeda.
- **Kutipan Sumber**: Setiap angka atau parameter yang diekstrak harus merujuk pada bagian spesifik dari paper asli (misalnya, *Tabel 2*, *Halaman 5, Kolom 2*).
