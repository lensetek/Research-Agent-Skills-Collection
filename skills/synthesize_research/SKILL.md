---
name: synthesize-research
description: >-
  Menganalisis, merangkum, dan mensintesis temuan dari beberapa publikasi ilmiah untuk menjawab pertanyaan riset tertentu secara komprehensif tanpa fabrikasi data.
---

# Synthesize Research

## Overview
Skill ini memandu Research Agent dalam menganalisis sekumpulan artikel ilmiah terkait topik tertentu, membandingkan hasilnya secara kritis, dan merangkum kesimpulan utama (konsensus, kontradiksi, dan arah masa depan) untuk menjawab pertanyaan riset pengguna secara faktual dan bebas dari halusinasi.

## Dependencies
Skill ini membutuhkan akses ke tools pencarian literatur:
- `literature-search-openalex`
- `pubmed-database` (untuk kesehatan/medis)
- `literature-search-arxiv` (untuk komputasi/fisika/matematika)
- `literature-search-biorxiv` (untuk biologi/kedokteran pra-cetak)

## Quick Start
Contoh penggunaan:
*"Gunakan skill synthesize-research untuk menganalisis dan mensintesis paper tentang dampak microplastic terhadap ekosistem laut."*

## Workflow

### 1. Perumusan Masalah & Kata Kunci
- Uraikan pertanyaan riset utama pengguna menjadi sub-pertanyaan yang lebih spesifik.
- Identifikasi kata kunci pencarian utama dan sinonimnya.

### 2. Pengumpulan Literatur Terverifikasi
- Lakukan pencarian literatur menggunakan tools dependensi.
- Kumpulkan minimal 5-10 artikel relevan yang memiliki metadata valid (judul, penulis, tahun, DOI/URL).
- **Penting:** Dilarang mengarang atau menggunakan artikel fiktif. Jika hasil pencarian tidak mencukupi, sampaikan ke pengguna dan minta arahan kata kunci baru.

### 3. Ekstraksi Temuan & Pembuatan Sintesis Matrix
- Baca abstrak atau isi makalah yang diperoleh.
- Buatlah tabel sintesis internal (Sintesis Matrix) yang memuat kolom:
  - Penulis & Tahun
  - Desain Eksperimen / Metodologi
  - Temuan Utama / Hasil
  - Kekuatan & Batasan (jika ada)

### 4. Penyusunan Laporan Sintesis (Synthesis Report)
- Tulis laporan dengan struktur ilmiah formal:
  - **Pendahuluan**: Latar belakang singkat dan pertanyaan riset yang dijawab.
  - **Analisis Tematis / Temuan Utama**: Kelompokkan temuan berdasarkan tema besar, bukan ringkasan per paper.
  - **Konsensus & Kontradiksi**: Jelaskan poin-poin di mana para peneliti sepakat, serta perdebatan atau hasil yang bertentangan antar studi.
  - **Kesimpulan & Celah Masa Depan**: Ringkasan jawaban atas pertanyaan riset dan apa yang belum terjawab.
- Gunakan sitasi dalam teks (in-text citation) seperti `(Penulis, Tahun)` atau `[1]` yang merujuk langsung ke Daftar Pustaka.

### 5. Daftar Pustaka Valid
- Cantumkan daftar referensi lengkap yang digunakan dengan tautan DOI atau URL asli di akhir laporan.

## Common Mistakes
- **Ringkasan Paralel**: Menulis laporan sebagai daftar ringkasan paper satu-satu (e.g., "Paper A menemukan X. Paper B menemukan Y.") tanpa mensintesis relasi antar paper tersebut.
- **Mengabaikan Kontradiksi**: Mengabaikan data atau paper yang hasilnya tidak mendukung hipotesis umum. Perbedaan hasil eksperimen wajib dibahas secara netral.
