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
Sesuai arahan pengguna, agen dibekali **kebebasan penuh** dalam mengimplementasikan metode scraping menggunakan strategi **Dual-Mode (Hibrida)**:
1. **Unrestricted Scraping (Speed First)**: Utamakan metode ringan seperti API resmi/tidak resmi atau HTTP requests statis (`urllib`, `requests`, atau `BeautifulSoup` di Python) karena jauh lebih cepat dan hemat sumber daya. Gunakan segala taktik penyamaran seperti memalsukan User-Agent dan penanganan session/cookies.
2. **Dynamic Content & Bot Protection Fallback (Robustness Second)**: Jika data dimuat secara dinamis via JavaScript, situs dilindungi bot protection (seperti Cloudflare dasar), atau memerlukan interaksi UI yang kompleks:
   - **WAJIB** beralih (*fallback*) ke browser automation menggunakan MCP server `chrome-devtools`.
   - Gunakan tool seperti `puppeteer_navigate`, `puppeteer_click`, atau `network_get_requests` untuk menginspeksi network payloads secara dinamis tanpa memparsing DOM kasar jika memungkinkan.
3. **Structured Storage**: Data hasil ekstraksi/scraping wajib disimpan secara rapi di dalam direktori proyek dalam format terstruktur: `.csv`, `.json`, atau database `.sqlite` (disesuaikan dengan ukuran data).
4. **Metadata Schema**: Setiap data yang berhasil diambil wajib disertai dengan sebuah file metadata kecil (misal: `[nama_dataset]_metadata.json`) yang mendokumentasikan:
   - Sumber URL asal.
   - Tanggal pengambilan data.
   - Penjelasan skema kolom/data.
5. **Anti-Hallucination & Anti-Mockup (FATAL)**: Dilarang keras membuat atau menghasilkan file CSV/JSON dummy/fiktif menggunakan kode statis (seperti membuat DataFrame buatan sendiri). Anda wajib menarik data sungguhan dari web/API yang dituju. Jika akses terblokir atau data gagal diekstrak setelah mencoba kedua mode, laporkan ERROR kepada pengguna dan hentikan proses.

## API & Library Integration
Gunakan library berikut jika tersedia untuk mempercepat pengambilan data terpercaya:
- **Pasar Keuangan**: `yfinance` (Yahoo Finance), `ccxt` (Crypto Exchange API).
- **Ekonomi & Sosial**: `pandas_datareader` (menghubungkan FRED, World Bank, OECD).
- **Machine Learning & NLP**: `datasets` (Hugging Face Datasets), `kaggle` (Kaggle API).

## Workflow Execution
1. **Identifikasi Kebutuhan**: Pahami data apa yang dicari oleh pengguna atau yang dibutuhkan oleh alur riset.
2. **Pemilihan Metode & Eksekusi Jalur Hibrida**:
   - **Langkah A (HTTP/API Mode)**: Rancang script Python menggunakan requests/BeautifulSoup untuk mengunduh data secara cepat.
   - **Langkah B (Chrome DevTools Fallback)**: Jika Langkah A terblokir, gagal merender konten dinamis, atau memicu halaman error, jalankan browser Chrome via `chrome-devtools` MCP untuk menavigasi halaman secara interaktif dan ambil datanya.
3. **Pembuatan Script Python / Otomatisasi DevTools**: Tulis script Python mandiri di folder proyek atau gunakan perintah visual DevTools untuk menangani seluruh proses pengambilan data dari awal hingga penyimpanan akhir.
4. **Eksekusi & Validasi**: Jalankan script atau proses otomatisasi tersebut, lalu pastikan file data yang dihasilkan valid dan tidak korup.
5. **Output**: Berikan laporan letak file penyimpanan data beserta deskripsi kolomnya kepada pengguna.

## Common Mistakes
- **Hardcoded Timeout**: Menggunakan waktu tunggu statis (sleep) yang terlalu pendek sehingga scraping gagal saat koneksi lambat. Gunakan penanganan waktu tunggu dinamis (explicit waits/DevTools dynamic load events).
- **Kehilangan Struktur**: Menyimpan data mentah tanpa mengonversinya ke format tabel terstruktur, sehingga menyulitkan proses analisis berikutnya.
- **Mengabaikan Captcha / Proteksi**: Langsung menyerah saat diblokir. Selalu gunakan fallback Chrome DevTools MCP untuk mensimulasikan sesi browser riil sebelum menyatakan kegagalan.

