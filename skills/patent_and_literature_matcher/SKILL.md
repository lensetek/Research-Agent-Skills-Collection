---
name: patent-and-literature-matcher
description: >-
  Membandingkan klaim invensi teknologi atau paten dengan literatur publikasi ilmiah yang ada untuk mengevaluasi kebaruan (novelty) dan potensi prior art.
---

# Patent & Literature Matcher

## Overview
Skill ini dirancang untuk membantu penemu, peneliti, dan spesialis kekayaan intelektual (IP) dalam mengidentifikasi apakah suatu invensi teknologi baru sudah pernah dipublikasikan sebelumnya dalam bentuk paper ilmiah (mendeteksi *prior art*). Agen memetakan klaim paten terhadap makalah-makalah ilmiah yang relevan dan menghitung kecocokan konsepnya untuk mengukur aspek kebaruan (*novelty*).

## Dependencies
- `literature-search-openalex`
- `literature-search-arxiv`
- `literature-search-europepmc`
- `pubmed-database`

## Quick Start
Contoh penggunaan:
*"Gunakan skill patent-and-literature-matcher untuk memverifikasi apakah klaim sistem pendingin baterai EV berbasis graphene di bawah ini sudah memiliki prior art di publikasi ilmiah."*

## Workflow

### 1. Dekonstruksi Klaim Invensi
- Baca deskripsi teknologi atau klaim paten yang diberikan oleh pengguna.
- Pecah klaim utama menjadi beberapa komponen kunci (misalnya: material yang digunakan, mekanisme kerja, aplikasi spesifik).

### 2. Formulasi Query Pencarian Paten & Literatur
- Buat query pencarian terarah berdasarkan komponen klaim tersebut.
- Lakukan pencarian literatur menggunakan tools database ilmiah (OpenAlex, arXiv, dll.).

### 3. Pemetaan & Pencocokan Klaim (Claim Mapping)
- Bandingkan setiap komponen klaim invensi dengan paper-paper ilmiah teratas hasil pencarian.
- Buat **claim-mapping table** untuk mendokumentasikan kecocokan:
  - Komponen Klaim Invensi (e.g., "Penggunaan graphene oxide coating")
  - Paper Ilmiah yang Relevan (e.g., "Smith et al., 2021 menemukan pelapisan graphene oxide pada...")
  - Status Kebaruan (e.g., Identik / Mirip / Baru)
  - Penjelasan & Batasan Perbandingan

### 4. Penilaian Risiko Prior Art
- Klasifikasikan tingkat risiko *prior art* secara keseluruhan:
  - **Tinggi**: Komponen klaim utama sangat mirip atau identik dengan publikasi yang sudah ada.
  - **Sedang**: Ada kesamaan konsep dasar, namun aplikasi atau metode implementasi spesifiknya berbeda.
  - **Rendah**: Konsep invensi belum ditemukan atau dipublikasikan dalam literatur ilmiah terindeks.

### 5. Penyusunan Laporan Evaluasi Kebaruan
Format laporan:
- **Ringkasan Eksekutif**: Penilaian tingkat risiko prior art dan status novelty.
- **Tabel Pemetaan Klaim**: Detail perbandingan komponen per komponen.
- **Ulasan Publikasi Relevan**: Analisis kritis terhadap paper-paper ilmiah yang paling mirip dengan invensi.
- **Rekomendasi Riset/Paten**: Langkah yang disarankan (misalnya mempersempit ruang lingkup klaim paten agar lebih spesifik).

## Common Mistakes
- **Hanya Mencocokkan Kata Kunci**: Menganggap riset identik hanya karena menggunakan kata kunci yang sama tanpa memahami konteks teknologi secara mendalam.
- **Klaim Parsial**: Hanya membandingkan satu aspek dari invensi dan mengabaikan aspek inovatif lainnya yang terintegrasi.
