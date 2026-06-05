---
name: discover-phenomenon-and-gap
description: >-
  Membantu mendeteksi fenomena ilmiah/teknologi baru yang sedang tren dan menganalisis celah penelitian (research gap) di sekitarnya berdasarkan publikasi terbaru.
---

# Discover Phenomenon and Gap

## Overview
Skill ini dirancang khusus untuk fase awal penelitian (eksplorasi). Tujuannya adalah memandu Research Agent dalam memindai literatur terbaru untuk mengidentifikasi fenomena baru (tren, anomali data, penemuan teknologi baru) dan merumuskan celah penelitian (*research gap*) konkret yang siap diteliti oleh pengguna.

## Dependencies
- `literature-search-openalex`
- `literature-search-arxiv`
- `literature-search-biorxiv`
- `pubmed-database`

## Quick Start
Contoh penggunaan:
*"Gunakan skill discover-phenomenon-and-gap untuk mengeksplorasi fenomena penggunaan model AI kolaboratif (multi-agent) dalam dunia pendidikan dan cari gap risetnya."*

## Workflow

### 1. Eksplorasi Fenomena Awal
- Lakukan pencarian literatur berbasis kata kunci luas untuk menangkap tren dalam 1–2 tahun terakhir.
- Identifikasi:
  * **Fenomena Utama**: Konsep, metode, atau perilaku baru yang banyak dilaporkan di paper terbaru.
  * **Anomali/Perdebatan**: Temuan eksperimen yang tidak biasa atau tidak sesuai dengan teori lama.

### 2. Analisis Kritis Literatur Terkini
- Cari paper dengan tipe "Review", "Survey", atau paper dengan sitasi cepat untuk memahami konsensus saat ini.
- Analisis bagian pembahasan (*discussion*) dan kesimpulan (*conclusion*) dari paper-paper tersebut untuk mencari pernyataan eksplisit seperti:
  * *"tapi mekanisme di balik X masih belum dipahami..."*
  * *"penelitian selanjutnya perlu menguji pada populasi/skala Y..."*
  * *"keterbatasan utama dari pendekatan ini adalah Z..."*

### 3. Pemetaan Celah Penelitian (Research Gap Extraction)
Klasifikasikan celah yang ditemukan ke dalam tipe berikut:
- **Celah Metodologis (Methodological Gap)**: Metode yang ada saat ini kurang akurat, terlalu lambat, atau belum diterapkan pada domain ini.
- **Celah Empiris (Empirical Gap)**: Kurangnya data eksperimen nyata untuk memverifikasi teori tertentu.
- **Celah Aplikasi (Application Gap)**: Teori/algoritma sudah ada tetapi belum pernah diujikan pada studi kasus atau industri tertentu.

### 4. Formulasi Usulan Pertanyaan Riset (Research Questions)
- Rumuskan 3–5 pertanyaan penelitian konkret (Research Questions/RQ) yang menjembatani fenomena yang ditemukan dengan celah penelitian tersebut.

### 5. Format Laporan Hasil Eksplorasi
Laporan harus memuat:
- **Identifikasi Fenomena**: Deskripsi fenomena yang diteliti beserta bukti rujukan ilmiahnya (judul paper, penulis, tahun, DOI).
- **Pemetaan Research Gaps**: Penjelasan detail tentang celah metodologis, empiris, atau aplikasi yang ditemukan.
- **Rekomendasi Pertanyaan Riset (RQ)**: Pertanyaan yang disarankan untuk dijawab dalam penelitian selanjutnya.

## Common Mistakes
- **Topik Terlalu Luas**: Tidak mempersempit fenomena (misal: membahas "AI secara umum" alih-alih "fenomena halusinasi pada LLM di domain hukum").
- **Gap yang Dibuat-buat (Fabricated Gap)**: Menyatakan ada gap padahal sebenarnya sudah banyak paper yang membahas solusi tersebut (kurang teliti dalam pencarian literatur).
