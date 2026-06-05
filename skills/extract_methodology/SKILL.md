---
name: extract-methodology
description: >-
  Membedah paper untuk mengekstrak detail teknis seperti metodologi, arsitektur model, parameter eksperimen, dataset, dan metrik kinerja secara presisi.
---

# Extract Methodology

## Overview
Skill ini ditujukan untuk membedah karya ilmiah secara mendalam guna menarik informasi metodologi eksperimen, alur algoritma/sistem, dataset yang digunakan, hyperparameter, dan hasil pengujian performa secara terstruktur. Ini sangat berguna ketika peneliti ingin mereproduksi (reproduce) penelitian terdahulu atau membandingkan baseline.

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

### 2. Pengambilan & Pembacaan Paper Lengkap
- Cari ID paper atau URL paper menggunakan tools pencarian literatur.
- Baca bagian Metode (Methodology), Pengaturan Eksperimen (Experimental Setup), dan Hasil (Results) pada paper target secara detail.

### 3. Ekstraksi Informasi Terstruktur
- Ekstrak informasi dan susun ke dalam format terstruktur (e.g., tabel markdown atau format JSON):
  - **Dataset**: Nama dataset, ukuran, pembagian train/val/test, dan teknik augmentasi data (jika ada).
  - **Arsitektur Model / Desain Sistem**: Lapisan jaringan, fungsi aktivasi, jumlah parameter, alur diagram sistem.
  - **Parameter Eksperimen**: Learning rate, batch size, epochs, optimizer (e.g., AdamW), loss function.
  - **Hasil & Metrik Evaluasi**: Skor performa model pada benchmark tertentu dibandingkan dengan model pembanding (baseline).

### 4. Analisis Reproduksibilitas (Reproducibility Check)
- Evaluasi apakah paper tersebut menyediakan informasi yang cukup untuk diimplementasikan ulang (reproduced):
  - Apakah kode sumber (source code) disediakan? (Cari link GitHub/GitLab).
  - Apakah dataset bersifat publik atau privat?
  - Apakah ada detail eksperimen yang ambigu atau tidak dijelaskan secara eksplisit?

### 5. Pelaporan Hasil Ekstraksi
- Buat rangkuman teknis yang bersih dan to-the-point menggunakan poin-poin terstruktur dan tabel data. Hindari narasi panjang lebar yang tidak perlu.

## Common Mistakes
- **Hanya Membaca Abstrak**: Abstrak jarang memuat detail teknis seperti hyperparameter atau detail dataset. Agen wajib menelusuri bagian isi utama paper.
- **Klaim Tanpa Bukti**: Menuliskan angka hasil performa atau parameter tanpa merujuk ke tabel atau bagian spesifik di dalam paper asli.
