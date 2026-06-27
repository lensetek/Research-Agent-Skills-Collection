---
name: journal-recommendation-finder
description: >-
  Membantu menemukan jurnal ilmiah yang tepat dan relevan untuk mempublikasikan hasil riset berdasarkan abstrak, kata kunci, ruang lingkup, dan faktor dampak jurnal.
---

# Journal Recommendation Finder

## Overview
Skill ini dirancang untuk membimbing Research Agent dalam mengidentifikasi dan mencocokkan naskah atau hasil penelitian pengguna dengan jurnal target publikasi yang tepat. Tujuannya adalah menyajikan alternatif jurnal yang kredibel, terindeks (internasional seperti Scopus/WoS maupun nasional seperti SINTA), dan memiliki kesesuaian ruang lingkup (*scope*) yang tinggi untuk memaksimalkan peluang diterimanya artikel ilmiah pengguna.

## Dependencies
- `literature-search-openalex`
- `pubmed-database`

## Quick Start
Contoh penggunaan:
*"Gunakan skill journal-recommendation-finder untuk merekomendasikan jurnal target publikasi (baik internasional terindeks Scopus/WoS maupun nasional terakreditasi SINTA) yang cocok bagi draf abstrak riset AI dalam medis di bawah ini."*

## Workflow

### 1. Analisis Naskah & Kata Kunci
- Baca judul, abstrak, dan kata kunci draf riset yang diberikan pengguna.
- Identifikasi konsep utama (*core concept*), metodologi utama, dan domain kontribusi riset tersebut.

### 2. Pencarian & Pencocokan Topik (Topic Alignment)
- Lakukan kueri pencarian paper-paper sejenis pada database akademik (e.g., OpenAlex).
- Identifikasi jurnal-jurnal mana saja yang paling sering menerbitkan paper dengan topik serupa dalam 2-3 tahun terakhir.

### 3. Evaluasi Kredibilitas & Metrik Jurnal Target
Kumpulkan data reputasi jurnal dari sumber terpercaya untuk meminimalkan risiko jurnal predator:
- **Indeksasi & Peringkat Internasional**: Secara default (*zero-configuration*), gunakan data dari **OpenAlex** untuk memeriksa status indeksasi dan kuartil Scopus (Q1/Q2/Q3/Q4), SJR (Scimago Journal Rank), atau Web of Science (WoS) Impact Factor/indeksasi.
- **Indeksasi & Peringkat Nasional (Indonesia)**: Jika targetnya adalah jurnal nasional, lakukan pencarian web/kueri ke portal resmi **SINTA Kemdikbud** untuk mendapatkan peringkat akreditasi jurnal (**SINTA 1 hingga SINTA 6**).
- **Model Akses**: Tentukan apakah jurnal bersifat *Open Access* (berbayar dengan APC) atau *Subscription* (gratis bagi penulis).
- **Turnaround Time**: Estimasi waktu review hingga keputusan pertama (biasanya dapat ditemukan di situs web resmi jurnal atau data statistik publikasi).

### 4. Penyusunan Rekomendasi Jurnal
Sajikan 3 hingga 5 rekomendasi jurnal alternatif dalam format tabel wajib berikut:
| Nama Jurnal | Penerbit | Kuartil (Scopus/WoS) / Peringkat SINTA | Tingkat Kesesuaian Scope (Tinggi/Sedang) | Estimasi Waktu Review (First Decision) | Biaya Publikasi (APC / Gratis) |
|---|---|---|---|---|---|

Berikan penjelasan singkat di bawah tabel mengenai alasan kecocokan tiap jurnal yang direkomendasikan dengan topik riset pengguna.

## Common Mistakes & Aturan Kritis
- **Membatasi Hanya pada Metrik Internasional**: Mengabaikan kebutuhan pengguna lokal Indonesia yang memerlukan akreditasi SINTA untuk publikasi ilmiah nasional. Selalu tawarkan opsi SINTA jika riset bertema lokal atau atas permintaan pengguna.
- **Hambatan API Key untuk Metrik Jurnal**: Menghentikan proses pencarian jika API Key Scopus atau Clarivate WoS tidak dikonfigurasi. Agen harus melakukan *fallback* dengan mengekstrak data kuartil dan SJR secara gratis menggunakan OpenAlex API.
- **Rekomendasi Jurnal Predator**: Merekomendasikan jurnal yang tidak terindeks atau masuk dalam daftar jurnal predator (Beall's List). Agen wajib selalu memprioritaskan penerbit bereputasi besar (e.g., IEEE, Elsevier, Springer, Wiley, MDPI, Taylor & Francis, atau penerbit universitas nasional terakreditasi SINTA 1-4).
- **Mengabaikan Biaya Publikasi (APC)**: Merekomendasikan jurnal Open Access dengan biaya APC (Article Processing Charge) sangat mahal tanpa memberikan informasi alternatif jurnal gratis (Subscription) kepada pengguna.
- **Ketidakcocokan Scope**: Hanya mencocokkan kata kunci secara dangkal tanpa membaca detail cakupan jurnal (*Journal Aims & Scope*), sehingga merekomendasikan jurnal yang salah fokus.
- **Data Metrik Kadaluarsa**: Menggunakan data peringkat kuartil (Q1-Q4) atau nilai impact factor lama yang sudah tidak valid. Tuliskan tahun pemutakhiran metrik yang dirujuk.
