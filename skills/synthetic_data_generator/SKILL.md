---
name: synthetic-data-generator
description: Bertugas sebagai Digital Twin / Persona Simulator untuk menghasilkan dataset sintetis (kuantitatif & kualitatif) dengan mensimulasikan responden penelitian berdasarkan profil demografis/psikografis tertentu.
---

# 🤖 Synthetic Data Generator (Digital Twin Simulator)

Skill ini memberikan agen kemampuan untuk bertindak sebagai **Simulator Responden** dalam penelitian. Agen akan mengadopsi persona (*digital twin*) berdasarkan parameter profil yang ditentukan dan merespons instrumen penelitian (kuisioner, skala Likert, pertanyaan wawancara terbuka) layaknya manusia.

## 🎯 Kapan Menggunakan Skill Ini?
- Ketika penelitian membutuhkan data primer yang besar (misalnya: survei dengan ratusan responden) namun terkendala waktu dan biaya.
- Ketika menguji rancangan model struktural (SEM/PLS) atau melatih model Machine Learning menggunakan data sintetis awal sebelum pengumpulan data asli.
- Ketika membutuhkan transkrip wawancara kualitatif sintetis dari berbagai sudut pandang persona.

## 🛠️ Instruksi Eksekusi

### 1. Inisialisasi Instrumen dan Profil
- **Instrumen:** Pahami struktur instrumen. Apakah ini kuantitatif (skala 1-5) atau kualitatif (jawaban naratif)?
- **Profil Demografi/Psikografi:** Pahami distribusi sampel target. Contoh: "Buat 300 data dengan distribusi 60% pria, 40% wanita, usia 18-35 tahun, tingkat skeptisisme teknologi tinggi-sedang."

### 2. Strategi Prompting Persona (LLM Adoption)
Untuk memastikan data tidak seragam dan memiliki varians yang realistis:
- Gunakan teknik *System Prompt* dinamis yang menyuntikkan sifat (*traits*) acak pada tiap iterasi responden.
- Terapkan *Temperature* yang cukup (misalnya 0.7 - 0.9) agar jawaban tidak deterministik.
- **Konsistensi Logis:** Pastikan jawaban antar item pertanyaan (terutama yang saling berkorelasi atau *reversed item*) konsisten dengan persona yang sedang dianut.
- **Attention Checks:** Jika diminta, sisipkan jawaban "jebakan" atau anomali wajar (misal: responden yang menjawab asal-asalan) dengan probabilitas kecil (misal 5%) untuk mensimulasikan *noise* dunia nyata.

### 3. Eksekusi Batch via Python (Wajib untuk Skala Besar)
Memanggil LLM satu per satu untuk ratusan responden sangat tidak efisien secara token dan waktu. Jika N > 10, **WAJIB** buat script Python yang memanfaatkan **Batch Prompting**.

**Panduan Alur Script Python:**
1. Buat prompt instruksi terpusat: *"Hasilkan 50 baris data berformat CSV. Setiap baris mewakili 1 responden unik. Kolom terdiri dari: Demografi, Q1, Q2, Q3 (skala 1-5) dan Opini (teks/kualitatif). Pastikan keragaman sesuai distribusi: [PROFIL_TARGET]. Output HANYA dalam format CSV valid tanpa markdown."*
2. Gunakan loop di Python untuk memanggil LLM (misalnya melalui `google-genai` atau endpoint LLM yang relevan) sebanyak N/50 kali.
3. Parsing string CSV hasil *generate* ke dalam struktur data (seperti `pandas.DataFrame`).
4. Gabungkan semua *batch* dan bersihkan baris yang *error/malformed*.
5. Simpan DataFrame akhir ke `synthetic_dataset.csv`.

### 4. Validasi Akhir dan Serah Terima
- Lakukan `describe()` sederhana via script untuk memastikan nilai Likert berada pada rentang yang valid (contoh: min 1, max 5) dan tidak ada *missing value* aneh.
- Serahkan file akhir kepada agen berikutnya (seperti `data-scientist-analyst`) beserta ringkasan statistik deskriptif singkat.
