---
name: data-acquisition-specialist
description: >-
  Bertugas mencari, mengumpulkan, mengunduh, dan melakukan web scraping data (baik statis maupun dinamis) dari berbagai sumber internet/API tanpa batasan guna menyusun dataset penelitian yang terstruktur.
---

# Data Acquisition Specialist

## Overview
Skill ini bertanggung jawab untuk pengumpulan dan penyediaan dataset mentah (*raw data*) yang dibutuhkan dalam penelitian ilmiah. Skill ini menggabungkan penggunaan library Python resmi (seperti `yfinance` untuk saham, `pandas-datareader` untuk data ekonomi FRED/World Bank, `ccxt` untuk kripto, dan `datasets` untuk machine learning) dengan penulisan script web scraping tingkat lanjut secara bebas dan tanpa batasan (*unrestricted scraping*) menggunakan BeautifulSoup, Selenium, Playwright, atau Scrapy.

## Dependencies
- Menggunakan library Python standar dan pihak ketiga untuk web scraping dan akuisisi data.
- Agen dapat menginstal dependensi Python yang kurang secara terprogram via terminal.

## Quick Start
Contoh penggunaan:
*"Gunakan skill data-acquisition-specialist untuk menyedot data historis laporan keuangan perusahaan X dari halaman web Y dan simpan dalam format CSV."*

## Web Scraping & Data Extraction Rules (ATURAN MUTLAK)
Sesuai arahan pengguna, agen dibekali **kebebasan penuh** dalam mengimplementasikan metode scraping:
1. **Unrestricted Scraping**: Gunakan segala metode yang diperlukan untuk menembus proteksi web (seperti memalsukan User-Agent, menggunakan *headless browser* (Selenium/Playwright), penundaan waktu dinamis, atau penanganan *session/cookies*).
2. **Dynamic Content Handling**: Jika data dimuat secara dinamis via JavaScript, wajib menggunakan *headless browser* (seperti Selenium) daripada parser HTML statis.
3. **Structured Storage**: Data hasil ekstraksi/scraping wajib disimpan secara rapi di dalam direktori proyek dalam format terstruktur: `.csv`, `.json`, atau database `.sqlite` (disesuaikan dengan ukuran data).
4. **Metadata Schema**: Setiap data yang berhasil diambil wajib disertai dengan sebuah file metadata kecil (misal: `[nama_dataset]_metadata.json`) yang mendokumentasikan:
   - Sumber URL asal.
   - Tanggal pengambilan data.
   - Penjelasan skema kolom/data.

## API & Library Integration
Gunakan library berikut jika tersedia untuk mempercepat pengambilan data terpercaya:
- **Pasar Keuangan**: `yfinance` (Yahoo Finance), `ccxt` (Crypto Exchange API).
- **Ekonomi & Sosial**: `pandas_datareader` (menghubungkan FRED, World Bank, OECD).
- **Machine Learning & NLP**: `datasets` (Hugging Face Datasets), `kaggle` (Kaggle API).

## Workflow Execution
1. **Identifikasi Kebutuhan**: Pahami data apa yang dicari oleh pengguna atau yang dibutuhkan oleh alur riset.
2. **Pemilihan Metode Terbaik**: Tentukan apakah menggunakan API/library resmi terlebih dahulu. Jika tidak ada, rancang script scraper (BeautifulSoup untuk statis, Selenium/Playwright untuk dinamis).
3. **Pembuatan Script Python**: Tulis script Python mandiri di folder proyek yang menangani seluruh proses pengambilan data dari awal hingga penyimpanan akhir.
4. **Eksekusi & Validasi**: Jalankan script tersebut (minta konfirmasi pengguna jika ada package Python yang perlu diinstal), lalu pastikan file data yang dihasilkan valid dan tidak korup.
5. **Output**: Berikan laporan letak file penyimpanan data beserta deskripsi kolomnya kepada pengguna.

## Common Mistakes
- **Hardcoded Timeout**: Menggunakan waktu tunggu statis (sleep) yang terlalu pendek sehingga scraping gagal saat koneksi lambat. Gunakan penanganan waktu tunggu dinamis (explicit waits).
- **Kehilangan Struktur**: Menyimpan data mentah tanpa mengonversinya ke format tabel terstruktur, sehingga menyulitkan proses analisis berikutnya.
- **Mengabaikan Captcha**: Menyerah saat menghadapi captcha. Upayakan mencari endpoint API tersembunyi (*hidden API endpoints*) di tab Network browser sebelum beralih ke scraping DOM kasar.
