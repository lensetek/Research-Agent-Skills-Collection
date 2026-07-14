---
name: synthetic-data-generator
description: Bertugas sebagai Digital Twin / Persona Simulator untuk menghasilkan dataset sintetis (kuantitatif & kualitatif) dengan mensimulasikan responden penelitian berdasarkan profil demografis/psikografis tertentu.
---

# Synthetic Data Generator (Digital Twin Simulator)

## Overview
Skill ini memberikan agen kemampuan untuk bertindak sebagai **Simulator Responden (Digital Twin Simulator)** dalam penelitian. Agen akan mengadopsi persona (*digital twin*) berdasarkan parameter profil yang ditentukan dan merespons instrumen penelitian (kuisioner, skala Likert, pertanyaan wawancara terbuka) layaknya responden manusia sesungguhnya. 

Selain menghasilkan data secara *offline* ke file CSV/JSON, skill ini juga mendukung **Active Participant Simulator**, yaitu kemampuan untuk mengotomatisasi pengisian kuesioner *online* nyata (seperti Google Forms, Typeform, dll.) melalui browser menggunakan integrasi MCP server `chrome-devtools`.

## Dependencies
- Modul Python standar (untuk pembuatan data offline skala besar).
- MCP Server `chrome-devtools` (untuk pengisian kuesioner online via browser).

## Quick Start
Contoh penggunaan:
1. *Offline*: *"Gunakan skill synthetic-data-generator untuk membuat dataset survei sintetis berisi 100 responden dengan profil demografi mahasiswa tingkat akhir dan respon terhadap kepuasan layanan bimbingan online."*
2. *Online*: *"Gunakan skill synthetic-data-generator untuk mensimulasikan 5 digital twin mengisi Google Form di URL https://forms.gle/xxxxx dengan profil pelaku UMKM digital."*

## Workflow

### 1. Inisialisasi Instrumen dan Profil
- **Instrumen:** Pahami struktur instrumen penelitian yang digunakan. Apakah ini kuantitatif (skala 1-5) atau kualitatif (jawaban naratif)?
- **Profil Demografi/Psikografi:** Pahami distribusi sampel target. Contoh: "Buat 300 data dengan distribusi 60% pria, 40% wanita, usia 18-35 tahun, tingkat skeptisisme teknologi tinggi-sedang."

### 2. Strategi Prompting Persona (LLM Adoption)
Untuk memastikan data tidak seragam dan memiliki varians yang realistis:
- Gunakan teknik *System Prompt* dinamis yang menyuntikkan sifat (*traits*) acak pada tiap iterasi responden.
- Terapkan *Temperature* yang cukup (misalnya 0.7 - 0.9) agar jawaban tidak deterministik.
- **Konsistensi Logis:** Pastikan jawaban antar item pertanyaan (terutama yang saling berkorelasi atau *reversed item*) konsisten dengan persona yang sedang dianut.
- **Attention Checks:** Jika diminta, sisipkan jawaban "jebakan" atau anomali wajar (misal: responden yang menjawab asal-asalan) dengan probabilitas kecil (misal 5%) untuk mensimulasikan *noise* dunia nyata.

### 3. Eksekusi Batch via Python (Wajib untuk Skala Besar Offline)
Memanggil LLM satu per satu untuk ratusan responden sangat tidak efisien secara token dan waktu. Jika N > 10 dan dijalankan secara offline, **WAJIB** buat script Python yang memanfaatkan **Batch Prompting**.

**Panduan Alur Script Python:**
1. Buat prompt instruksi terpusat: *"Hasilkan 50 baris data berformat CSV. Setiap baris mewakili 1 responden unik. Kolom terdiri dari: Demografi, Q1, Q2, Q3 (skala 1-5) dan Opini (teks/kualitatif). Pastikan keragaman sesuai distribusi: [PROFIL_TARGET]. Output HANYA dalam format CSV valid tanpa markdown."*
2. Gunakan loop di Python untuk memanggil LLM (misalnya melalui `google-genai` atau endpoint LLM yang relevan) sebanyak N/50 kali.
3. Parsing string CSV hasil *generate* ke dalam struktur data (seperti `pandas.DataFrame`).
4. Gabungkan semua *batch* dan bersihkan baris yang *error/malformed*.
5. Simpan DataFrame akhir ke `synthetic_dataset.csv`.

### 4. Pengisian Kuesioner Online (Active Participant Simulator)
Jika pengguna meminta untuk mengisi kuesioner online seperti Google Forms:
1. **Analisis Halaman (Form Mapping)**: Hubungkan ke server `chrome-devtools` dan arahkan browser ke URL kuesioner menggunakan `puppeteer_navigate`. Identifikasi tipe pertanyaan (text input, radio button, checkbox) menggunakan `puppeteer_evaluate`.
2. **Batching Responden**: Untuk setiap digital twin (misal N responden):
   - Hasilkan profil jawaban responden secara internal (dalam format JSON/Key-Value).
   - Temukan elemen input yang cocok dengan pertanyaan.
   - **Simulasi Input Manusia**:
     - Untuk pilihan ganda/skala Likert, gunakan `puppeteer_click` pada radio button yang sesuai.
     - Untuk isian teks, gunakan `puppeteer_type` untuk mengetik jawaban secara natural.
     - Tambahkan jeda waktu acak (human-like delay) antara 1,5 hingga 3 detik sebelum mengklik tombol kirim/berikutnya untuk meniru perilaku manusia dan menghindari deteksi anti-bot.
   - Klik tombol "Kirim" / "Submit" menggunakan `puppeteer_click`.
   - Ambil screenshot halaman sukses pengisian (`puppeteer_screenshot`) sebagai bukti validasi.
   - Jika ingin mengisi responden berikutnya, klik tautan "Kirim tanggapan lain" / "Submit another response" untuk memuat form baru.

### 5. Validasi Akhir dan Serah Terima
- **Offline**: Lakukan `describe()` sederhana via script untuk memastikan nilai Likert berada pada rentang yang valid (contoh: min 1, max 5) dan tidak ada *missing value* aneh.
- **Online**: Berikan ringkasan log sukses pengisian (misal: "3/3 Responden berhasil mengisi Google Form") beserta file screenshot bukti pengiriman untuk masing-masing responden.

## Common Mistakes & Aturan Kritis
- **Data Terlalu Seragam (No Variance)**: Menghasilkan respon data yang monoton atau tanpa variasi karena menggunakan suhu (*temperature*) LLM 0 atau sistem instruksi yang terlalu kaku.
- **Ketidakkonsistenan Persona**: Mengabaikan logika internal dari responden (misalnya, responden yang memiliki profil "gaptek/skeptis teknologi" namun memberikan respon sangat mahir dan antusias terhadap adopsi AI).
- **Format File Rusak (Malformed CSV)**: Menyimpan output dalam format CSV yang tidak valid sehingga gagal dibaca oleh agen pengolah data.
- **Deteksi Bot pada Form Online**: Mengisi form terlalu cepat tanpa jeda waktu, yang memicu munculnya CAPTCHA. Selalu gunakan penundaan dinamis (*randomized delay*) saat meniru input manusia.
