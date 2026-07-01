---
name: discover-phenomenon-and-gap
description: >-
  Membantu mendeteksi fenomena ilmiah/teknologi baru yang sedang tren dan menganalisis celah penelitian (research gap) di sekitarnya berdasarkan publikasi terbaru.
---

# Discover Phenomenon and Gap

## Overview
Skill ini dirancang khusus untuk fase awal penelitian (eksplorasi). Tujuannya adalah memandu Research Agent dalam memindai literatur terbaru untuk mengidentifikasi fenomena baru (tren, anomali data, penemuan teknologi baru) dan merumuskan celah penelitian (*research gap*) konkret yang valid dan dapat dipertanggungjawabkan secara akademik.

## Dependencies
- `literature-search-openalex`
- `literature-search-arxiv`
- `literature-search-biorxiv`
- `pubmed-database`

## Quick Start
Contoh penggunaan:
*"Gunakan skill discover-phenomenon-and-gap untuk mengeksplorasi fenomena penggunaan model AI kolaboratif (multi-agent) dalam dunia pendidikan dan cari gap risetnya."*

## Workflow
Pilih salah satu mode kerja di bawah ini berdasarkan arahan pengguna atau kebutuhan riset:

### Mode A: Literature-Driven Gap Discovery (Bawaan)
1. **Eksplorasi Fenomena Awal**: Lakukan pencarian literatur berbasis kata kunci luas untuk menangkap tren dalam 1–2 tahun terakhir. Identifikasi Fenomena Utama dan Anomali/Perdebatan teoretis.
2. **Analisis Kritis Literatur (Survey of Surveys & Batching)**:
   - *Survey of Surveys*: Prioritaskan 5-10 paper tipe "Review" atau "Survey" terbaru. Ekstrak bagian *Future Works*, *Discussion*, atau *Open Challenges*.
   - *Batch Processing*: Jika memproses paper primer (>10), lakukan bertahap (5 paper per siklus), catat temuan keterbatasan ke `temp_limitations_log.md`.
3. **Pemetaan Celah Penelitian (Gap)**: Klasifikasikan celah yang ditemukan (*Phenomenon, Theoretical, Methodological, Empirical, Performance, atau Evaluation Gap*).
4. **Formulasi RQ**: Rumuskan 3–5 pertanyaan penelitian konkret yang menjembatani fenomena dengan gap tersebut.

### Mode B: Dataset-Driven Ideation (Data Descriptors) - BARU
1. **Pencarian Data Descriptor**:
   - Lakukan pencarian terarah menggunakan `literature-search-openalex`, `pubmed-database`, atau `literature-search-arxiv` untuk menemukan paper tipe *Data Descriptor* atau *Dataset Paper* terbaru (1-2 tahun terakhir). Gunakan kata kunci pendukung seperti `"data descriptor"`, `"dataset descriptor"`, `"scientific data"`, atau `"data in brief"`.
2. **Potensi 1: Ekstraksi Rekomendasi Penulis Asli (Usage Notes)**:
   - Baca teks lengkap/abstrak (terutama bagian *Usage Notes*, *Value of the Data*, *Discussion*, atau *Reusability*).
   - Ekstrak gagasan riset turunan atau skenario penggunaan masa depan yang secara eksplisit disarankan oleh penulis asli dataset tersebut.
3. **Potensi 2: Eksplorasi Variabel-Metode Baru (Novelty Matrix)**:
   - Bedah skema dataset dan identifikasi variabel/fitur utama (misal: Variabel A, B, C).
   - Dapatkan keahlian metodologi atau algoritma pilihan pengguna (misal: "Random Forest" atau "Causal Inference").
   - Lakukan pencarian literatur kilat untuk menguji kebaruan (*novelty check*): *"Apakah sudah ada studi yang menghubungkan Variabel A dan C menggunakan metode pilihan pengguna pada dataset ini?"* Jika belum ada, rumuskan menjadi usulan ide baru.

---

## Format Laporan Hasil Eksplorasi

### Jika menggunakan Mode A (Literature-Driven):
1. **Fenomena Utama**: Isu ilmiah, teknologi, atau sosial baru yang sedang muncul.
2. **Bukti Tren**: Daftar rujukan ilmiah pendukung (judul, penulis, tahun, DOI).
3. **Masalah yang Belum Selesai**: Tantangan/keterbatasan yang belum dipecahkan.
4. **Jenis Gap**: Klasifikasi celah (*Phenomenon/Theoretical/Methodological/Empirical/Performance/Evaluation Gap*).
5. **Potensi Kontribusi**: Nilai tambah riset baru untuk menutup celah tersebut.
6. **Risiko Topik & Skala Kesulitan**: Analisis ketersediaan data dan skala kesulitan: **[ Trivial / Moderate / Hardcore ]**.

### Jika menggunakan Mode B (Dataset-Driven):
1. **Source Data Descriptor**: Judul paper descriptor, penulis, tahun, DOI, dan tautan repositori penyimpanan data asli (Zenodo, Figshare, Dryad, dll.).
2. **Karakteristik Dataset**: Ringkasan variabel/fitur utama, format file, dan ukuran data.
3. **Opsi Potensi 1 (Rekomendasi Penulis Asli)**: Daftar ide riset turunan yang disarankan langsung di dalam paper.
4. **Opsi Potensi 2 (Inovasi Hubungan Variabel)**: Usulan korelasi antar-variabel baru yang dipadukan dengan metode pilihan pengguna, lengkap dengan analisis kebaruan singkat (kroscek literatur).
5. **Rekomendasi Eksekusi**: Langkah awal memuat dataset dan estimasi skala kesulitan: **[ Trivial / Moderate / Hardcore ]**.

---

## Common Mistakes & Aturan Kritis
- **Gap yang Dibuat-buat (Fabricated Gap)**: Menyatakan ada gap/novelty padahal sudah banyak paper yang membahas solusi tersebut. Wajib melakukan kueri pencarian sebelum menyimpulkan ketiadaan studi.
- **Argumen Gap yang Lemah**: Menyebut sesuatu sebagai gap/novelty *hanya* karena belum diteliti di lokasi/konteks tertentu, kecuali jika perbedaan lokasi tersebut secara ilmiah terbukti mempengaruhi perilaku data.
- **Mengabaikan Tautan Repositori**: Dalam Mode B, menyajikan ide riset tanpa menyertakan tautan repositori data asli yang dapat diakses langsung oleh pengguna. Data harus dapat diunduh secara nyata.

