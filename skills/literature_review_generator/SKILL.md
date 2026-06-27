---
name: literature-review-generator
description: >-
  Melakukan tinjauan pustaka terstruktur, menyusun kronologi perkembangan riset, dan mengidentifikasi celah penelitian (research gaps) pada topik tertentu.
---

# Literature Review Generator

## Overview
Skill ini dirancang untuk menghasilkan tinjauan pustaka (literature review) yang sistematis, mendalam, dan memiliki bobot argumentasi ilmiah yang kuat. Agen akan membantu memetakan perkembangan riset dari waktu ke waktu, mengidentifikasi kontradiksi/konsensus, dan secara logis membangun argumentasi yang menjustifikasi mengapa penelitian baru yang diusulkan bernilai penting untuk dilakukan.

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

### 1. Perencanaan Protokol Review & Penentuan Mode
Tentukan batasan review (rentang tahun, tipe dokumen) dan pilih salah satu mode kerja berikut:
- **Narrative Literature Review Mode**: Untuk proposal konseptual atau penyusunan bab teori umum.
- **Systematic Literature Review (SLR) Mode**: Diwajibkan untuk riset berskala besar (>100 paper). Menggunakan kriteria inklusi-eksklusi formal, skrip penyaringan otomatis, dan alur PRISMA 4-tahap yang dicatat ke dalam *checkpoint* CSV (Lihat bagian khusus Alur PRISMA di bawah).
- **Thematic Review Mode**: Mengelompokkan paper berdasarkan tema, konsep, atau sub-topik masalah.
- **Chronological Review Mode**: Menelusuri sejarah perkembangan ide/teknologi dari pionir awal hingga tren termutakhir untuk menunjukkan evolusi paradigma.
- **Critical Review Mode**: Berfokus mengevaluasi kelemahan asumsi teoretis, kelemahan evaluasi, bias data, dan keterbatasan metodologis dari studi sebelumnya.

### 2. Alur Kerja PRISMA & Checkpointing (Khusus SLR Mode Skala Besar)
Jika mode **Systematic Literature Review (SLR)** dipilih untuk menangani pencarian dalam jumlah besar (ribuan paper), agen WAJIB menggunakan metode penyaringan programatik (*Programmatic Screening*) untuk menghindari ekskusi manual LLM yang memboroskan token. Alur 4 tahap ini harus dipatuhi dan disimpan dalam berkas CSV (*checkpoint*):

1. **Identification (Tarik Metadata)**: Panggil API mesin pencari terbuka yang bersifat gratis dan *zero-configuration* (`literature-search-openalex`, `literature-search-arxiv`, `pubmed-database`, dll.) untuk HANYA mengambil metadata (Judul, Abstrak, Penulis, Tahun, DOI) dari ribuan hasil secara terintegrasi. DILARANG MENGUNDUH TEKS PENUH. Simpan luaran mentah ke `prisma_1_identification.csv`. **DILARANG KERAS MENGHASILKAN DATA MOCKUP/DUMMY**. Anda WAJIB menggunakan modul `requests` di Python untuk menembak endpoint API asli atau mendelegasikan tugas ke agen pencari sungguhan. Terapkan mekanisme *Retry/Backoff* (maksimal 3 kali pengulangan jika terjadi `Timeout`). Jika tetap gagal, Anda harus MELAPORKAN ERROR dan BERHENTI, bukan mengarang data.
2. **Automated Screening (Python Filter)**: Tulis dan jalankan skrip Python (menggunakan Pandas) untuk menyaring `prisma_1_identification.csv`. Buang duplikat, batasi rentang tahun, dan eliminasi paper yang teks judul/abstraknya sama sekali tidak mengandung kata kunci utama. Simpan sisa paper yang lolos seleksi otomatis ke `prisma_2_screened.csv`.
3. **Eligibility (Semantic & Quality Audit)**: Untuk kumpulan paper yang tersisa (50-100 paper), gunakan LLM untuk membaca abstrak guna memastikan relevansi semantik terhadap *Inclusion/Exclusion criteria*. Gunakan agen `source-quality-appraiser` untuk membuang paper berpemeringkatan rendah/predator. Simpan paper yang benar-benar relevan ke `prisma_3_eligible.csv`.
4. **Included (Ekstraksi Teks Penuh)**: Unduh PDF/teks penuh gratis (terutama paper bertipe Open Access) dari kumpulan akhir (e.g. 20-40 paper) menggunakan Core API atau OpenAlex OA link, dan gunakan `extract-methodology` untuk membedah parameternya. Simpan matriks sintesis akhir ke `prisma_4_included.csv`.
5. **Diagram PRISMA**: Agen diwajibkan untuk menutup tahapan ini dengan men-generate diagram alir (Flowchart) PRISMA visual dalam format **Mermaid diagram**, yang menunjukkan penyusutan jumlah paper (n) di setiap tahap (Identification -> Screening -> Eligibility -> Included).

### 3. Penelusuran & Pemetaan Historis (Timeline)
- Cari literatur pionir (seminal papers) dan paper ulasan (survey papers) terbaru menggunakan mesin pencari literatur.
- Susun garis waktu kronologis perkembangan riset tersebut.

### 4. Analisis Celah Penelitian & Argument Map
- Buat **Argument Map** untuk membangun alur argumentasi yang menjustifikasi posisi riset baru. Contoh alur:
  * *Riset terdahulu banyak fokus pada akurasi metodologi X.*
  * *Namun, evaluasi akurasi tersebut sering tidak menguji robustness dalam kondisi riil.*
  * *Beberapa paper menggunakan dataset yang tidak seimbang tanpa penanganan bias.*
  * *Oleh karena itu, riset baru ini hadir untuk menutup gap tersebut dengan menawarkan evaluasi robustness berbasis ablation.*

### 5. Format Laporan Literature Review
Struktur penulisan tinjauan pustaka harus memuat:
- **Pendahuluan**: Urgensi topik, pertanyaan riset yang dipecahkan, dan batasan review.
- **Matriks Ringkasan Literatur**: Tabel terstruktur wajib dengan kolom berikut:
  | Tahun | Penulis | Fokus Riset | Metode | Dataset / Konteks | Temuan Utama | Keterbatasan Utama | Relevansi dengan Riset Kita |
  |---|---|---|---|---|---|---|---|
- **Argument Map (Peta Posisi Penelitian)**: Penjelasan berbasis poin-poin alur argumentasi yang mengarah pada kontribusi riset Anda.
- **Analisis Kritis & Kategorisasi Tema**: Pengelompokan literatur secara kritis berdasarkan pendekatan yang digunakan (e.g., pendekatan berbasis aturan vs deep learning).
- **Kesimpulan**: Ringkasan implikasi teoritis dan metodologis untuk riset mendatang.

### 6. Sitasi & Referensi
- Pastikan setiap klaim didukung oleh referensi yang tepat dengan mencantumkan metadata DOI/URL yang valid pada Daftar Pustaka.

## Common Mistakes & Aturan Kritis
- **Halusinasi Data & Pemalsuan DOI (FATAL)**: Dilarang keras menciptakan paper fiktif sekadar untuk memenuhi tabel PRISMA. Pembuatan *DataFrame* berisi judul paper karangan adalah pelanggaran fatal. Setiap paper wajib bersumber dari API nyata dan memiliki tautan DOI yang valid.
- **Memaksa Pengguna Memasukkan API Key Rumit**: DILARANG keras menampilkan pesan error yang memaksa pengguna mengonfigurasi API Key secara manual jika API Key (seperti Semantic Scholar) belum ada. Sebaliknya, gunakan API gratisan yang beroperasi tanpa kunci (seperti OpenAlex, PubMed, arXiv) atau arahkan pengguna secara ramah via chat untuk membantu memasukkannya jika kuota tinggi benar-benar dibutuhkan.
- **Hanya Merangkum Tanpa Mengkritik**: Menghindari model penulisan deskriptif daftar ringkasan (e.g., "Peneliti A menemukan X. Peneliti B menemukan Y."). Agen harus membandingkan, mengelompokkan, dan mengkritisi.
- **Kronologi Acak**: Menulis sejarah konsep tanpa urutan waktu yang jelas.
- **Referensi Tidak Valid**: Menulis kutipan tanpa menyertakan DOI atau tautan referensi asli yang dapat dilacak. Dilarang keras mengarang referensi.
