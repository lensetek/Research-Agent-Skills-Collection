---
name: literature-review-generator
description: >-
  Melakukan tinjauan pustaka terstruktur, menyusun kronologi perkembangan riset, dan mengidentifikasi celah penelitian (research gaps) pada topik tertentu.
---

# Literature Review Generator

## Overview
Skill ini dirancang untuk menghasilkan tinjauan pustaka (literature review) yang sistematis dan mendalam. Agen akan melacak tren penelitian dari waktu ke waktu, memetakan kontribusi utama para peneliti terkemuka, dan mengidentifikasi celah (gaps) dalam literatur saat ini yang dapat dijadikan peluang riset baru.

## Dependencies
- `literature-search-openalex`
- `literature-search-arxiv`
- `pubmed-database`
- `literature-search-biorxiv`
- `literature-search-europepmc`

## Quick Start
Contoh penggunaan:
*"Gunakan skill literature-review-generator untuk memetakan perkembangan algoritma reinforcement learning dari tahun 2018 hingga sekarang dan cari research gaps yang ada."*

## Workflow

### 1. Perencanaan Protokol Review
- Definisikan batasan tinjauan pustaka: rentang tahun publikasi, tipe dokumen (jurnal, konferensi), dan area sub-topik spesifik.
- Buat kriteria inklusi/eksklusi paper secara logis (misalnya hanya menyertakan paper dengan sitasi tinggi atau paper eksperimental).

### 2. Penelusuran & Pemetaan Historis (Timeline)
- Cari literatur pionir (seminal papers) dan paper ulasan (review papers) terbaru menggunakan mesin pencari literatur.
- Susun garis waktu kronologis perkembangan riset tersebut, menyoroti peralihan paradigma (paradigm shifts) atau terobosan metodologi penting dari tahun ke tahun.

### 3. Analisis Celah Penelitian (Research Gap Analysis)
- Analisis area-area yang:
  - Memiliki hasil eksperimen yang saling bertentangan.
  - Memiliki keterbatasan asumsi teoritis yang belum diuji secara empiris.
  - Kurang dieksplorasi karena keterbatasan teknologi masa lalu.
  - Memiliki aplikasi praktis yang belum banyak diteliti.
- Dokumentasikan celah ini secara jelas dalam bab atau bagian khusus bertajuk **"Research Gaps & Future Work"**.

### 4. Penyusunan Naskah Literature Review
Struktur penulisan tinjauan pustaka:
- **Pendahuluan**: Urgensi topik dan ruang lingkup review.
- **Perkembangan Historis / Landasan Teori**: Kronologi perkembangan konsep.
- **Kategorisasi Tema / Taksonomi Riset**: Pengelompokan literatur berdasarkan metodologi atau pendekatan yang digunakan (e.g., pendekatan berbasis aturan vs deep learning).
- **Analisis Kritis & Celah Penelitian**: Pembahasan kelemahan metodologi terdahulu dan peluang riset baru.
- **Kesimpulan**: Ringkasan arah penelitian selanjutnya.

### 5. Sitasi & Referensi
- Pastikan setiap klaim didukung oleh referensi yang tepat dengan mencantumkan metadata DOI/URL yang valid pada Daftar Pustaka.

## Common Mistakes
- **Hanya Merangkum Tanpa Mengkritik**: Hanya menulis ulang apa yang dilakukan paper tanpa membandingkan kelebihan dan kekurangan metodologinya secara kritis.
- **Kronologi Acak**: Menulis sejarah perkembangan teknologi tanpa urutan waktu yang runtut, membuat pembaca sulit melihat evolusi ide riset.
