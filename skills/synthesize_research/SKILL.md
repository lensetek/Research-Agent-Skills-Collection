---
name: synthesize-research
description: >-
  Menganalisis, merangkum, dan mensintesis temuan dari beberapa publikasi ilmiah untuk menjawab pertanyaan riset tertentu secara komprehensif tanpa fabrikasi data.
---

# Synthesize Research

## Overview
Skill ini memandu Research Agent dalam menganalisis sekumpulan artikel ilmiah terkait topik tertentu, membandingkan hasilnya secara kritis, menilai kekuatan metodologi masing-masing bukti, dan merangkum kesimpulan utama (konsensus, kontradiksi, implikasi, dan arah masa depan) untuk menghasilkan sintesis ilmiah objektif dan bebas dari halusinasi.

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
- Kumpulkan minimal 5-10 artikel ilmiah dengan metadata valid (judul, penulis, tahun, DOI/URL).
- **Penting:** Dilarang mengarang artikel fiktif. Jika hasil tidak mencukupi, sampaikan apa adanya ke pengguna.

### 3. Ekstraksi Temuan & Verification Grounding
- Lakukan sintesis kritis dengan membandingkan temuan antar-paper, menilai kekuatan bukti masing-masing studi (dilihat dari ukuran dataset, ketegasan evaluasi, atau validitas metode), dan mengidentifikasi pola hasil eksperimen.
- **Verification Grounding (WAJIB)**: Semua klaim temuan utama wajib divalidasi terhadap teks asli paper rujukan menggunakan skrip `fetch_evidence_snippet.py` untuk memastikan bahwa klaim sintesis didukung 100% oleh kutipan verbatim asli paper (*Evidence Snippet*).

### 4. Penyusunan Laporan Sintesis (Synthesis Report)
Tulis laporan dengan struktur ilmiah formal sebagai berikut:
- **Pendahuluan**: Latar belakang singkat dan pertanyaan riset yang dijawab.
- **Tabel Sintesis Temuan Utama (Synthesis Table)**: Wajib membuat tabel dengan kolom:
  | Pertanyaan Riset | Sintesis Temuan | Bukti Utama (Referensi Paper) | Kontradiksi / Perdebatan | Implikasi Praktis/Teoris | Keterbatasan Sintesis |
  |---|---|---|---|---|---|
- **Analisis Tematik / Konsensus & Kontradiksi**: Kelompokkan temuan berdasarkan tema besar. Jelaskan secara netral aspek mana yang disepakati para peneliti dan aspek mana yang menunjukkan hasil saling bertentangan beserta faktor pemicunya (misal: perbedaan ukuran sampel atau variansi metode pengujian).
- **Kesimpulan**: Ringkasan jawaban atas pertanyaan riset utama.

### 5. Daftar Pustaka Valid
- Cantumkan referensi lengkap dengan tautan DOI atau URL asli di akhir laporan.

## Common Mistakes & Aturan Kritis (Anti-Halusinasi & Sintesis)
- **Ringkasan Paralel**: Menghindari model penulisan deskriptif berurutan (e.g., "Paper A menemukan X. Paper B menemukan Y."). Agen harus merelasikan dan membandingkan temuan secara sintesis.
- **Halusinasi Metrik & Perbandingan Keliru**: 
  - Dilarang menggabungkan atau membandingkan langsung metrik yang tidak sebanding dari paper yang berbeda.
  - Dilarang menarik kesimpulan model/algoritma terbaik secara mutlak jika dataset dan skenario pengujiannya berbeda.
- **Mengabaikan Hasil Kontradiktif**: Perbedaan hasil eksperimen antar-studi wajib diulas secara objektif tanpa bias.
- **Pemisahan Opini**: Wajib memisahkan secara jelas antara temuan faktual yang dilaporkan di paper dan interpretasi/analisis subjektif agen. Gunakan frasa penjelas seperti *"Berdasarkan bukti di atas, analisis kami menunjukkan bahwa..."*.
