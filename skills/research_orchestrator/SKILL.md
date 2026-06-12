---
name: research-orchestrator
description: >-
  Berperan sebagai starter utama yang mengoordinasikan seluruh alur kerja riset secara otomatis dari eksplorasi topik, penentuan gap, metodologi, sintesis literatur, hingga kesiapan publikasi.
---

# Research Orchestrator (Starter Skill)

## Overview
Skill ini adalah pintu masuk utama (*starter/entry point*) untuk mengotomatiskan seluruh alur kerja riset pada **Research-Agent**. Ketika pengguna mengaktifkan skill ini dengan memberikan ide riset kasar atau domain umum, agen akan mengorkestrasikan dan memanggil 13 skill pendukung lainnya secara berurutan, mengirimkan output dari satu tahap sebagai input ke tahap berikutnya, dan menyajikan laporan akhir berupa *Research Dashboard* terintegrasi.

Secara khusus, skill ini mendukung **Implicit Personalization**. Di awal eksekusi, agen wajib memeriksa keberadaan berkas `user_profile.json` di root direktori untuk memuat preferensi pengguna. Di akhir eksekusi, agen akan menganalisis umpan balik pengguna dan memperbarui berkas tersebut secara otomatis.

## Dependencies
Skill ini mengoordinasikan eksekusi dari 13 skill berikut:
1. `discover-phenomenon-and-gap`
2. `research-question-builder`
3. `hypothesis-or-proposition-builder`
4. `research-design-planner`
5. `literature-review-generator`
6. `extract-methodology`
7. `source-quality-appraiser`
8. `citation-and-reference-validator`
9. `paper-matrix-builder`
10. `synthesize-research`
11. `patent-and-literature-matcher`
12. `journal-recommendation-finder`
13. `academic-peer-reviewer`
14. `reviewer-response-and-revision`

## Quick Start
Contoh penggunaan:
*"Gunakan skill research-orchestrator untuk memulai riset otomatis penuh tentang efektivitas metode deteksi penipuan transaksi berbasis grafik (Graph Neural Networks)."*

## Orchestration Workflow

Agen wajib mengikuti alur eksekusi otomatis 5 fase berikut secara beruntun:

```text
[Baca Profil] ──> [Fase 1: Masalah] ──> [Fase 2: Metodologi] ──> [Fase 3: Literatur] ──> [Fase 4: Publikasi] ──> [Fase 5: Personalization]
```

### Persiapan Awal (Load Profile)
0. Periksa apakah berkas `user_profile.json` ada di root direktori proyek. Jika ada, baca preferensi penelitian (gaya penulisan, jurnal target, metodologi yang disukai) dan gunakan sebagai panduan default dalam setiap fase riset di bawah ini.

### Fase 1: Eksplorasi & Pembingkaian Masalah
1.  Terima topik/ide awal dari pengguna.
2.  Jalankan `discover-phenomenon-and-gap` untuk memetakan fenomena tren terbaru dan merumuskan celah ilmiah (*research gap*) konkret.
3.  Kirimkan hasil gap tersebut ke `research-question-builder` untuk merumuskan Pertanyaan Penelitian (RQ), Tujuan, dan Kontribusi riset.
4.  Kirimkan hasil RQ ke `hypothesis-or-proposition-builder` untuk merancang kerangka konseptual teoretis serta hipotesis/proposisi yang akan diuji.

### Fase 2: Perencanaan Metodologi
5.  Kirimkan seluruh dokumen luaran Fase 1 ke `research-design-planner` untuk menyusun detail metodologi eksperimen, penentuan sampling/variabel, alur pengujian data, serta skenario pengujian ketahanan (*robustness/ablation*).

### Fase 3: Kajian & Validasi Literatur
6.  Jalankan `literature-review-generator` untuk memetakan perkembangan riset historis dan menyusun argumentasi posisi riset baru.
7.  Gunakan `extract-methodology` untuk mengekstrak data teknis dari paper-paper rujukan utama hasil pencarian.
8.  Jalankan `source_quality_appraiser` untuk mengaudit tingkat kredibilitas jurnal rujukan (kuartil Scopus/CORE ranking) guna menyaring paper yang lemah metodologinya.
9.  Jalankan `citation-and-reference-validator` untuk memverifikasi keakuratan DOI dan memastikan klaim naskah didukung secara faktual oleh paper referensi (bebas halusinasi sitasi).
10. Jalankan `paper-matrix-builder` untuk merangkum seluruh parameter teknis rujukan ke dalam Tabel State-of-the-Art (SotA) yang terstandarisasi.

### Fase 4: Sintesis & Kesiapan Publikasi
11. Jalankan `synthesize-research` untuk menyatukan seluruh bukti temuan literatur, memetakan konsensus, serta mengulas kontradiksi secara kritis.
12. Jalankan `patent-and-literature-matcher` untuk memverifikasi kebaruan (*novelty*) klaim invensi terhadap potensi *prior art*.
13. Jalankan `journal-recommendation-finder` untuk memberikan rekomendasi target jurnal ilmiah (Q1-Q4) yang paling cocok dengan ruang lingkup riset.
14. Jalankan `academic-peer-reviewer` untuk mensimulasikan proses penelaahan sejawat (*peer review*) guna memberikan penilaian kritis, daftar masalah (mayor/minor), serta rekomendasi kelayakan publikasi sebelum dikirim ke jurnal resmi.
15. (Opsional/Jika ada perbaikan) Jalankan `reviewer-response-and-revision` untuk membimbing langkah-langkah revisi naskah.

### Fase 5: Pembaruan Profil & Memori Riset (Implicit Personalization)
16. Evaluasi seluruh sesi interaksi, komentar, dan umpan balik eksplisit maupun implisit dari pengguna (misalnya: penolakan jurnal tertentu, koreksi atas gaya penulisan, atau preferensi metode analisis data).
17. Perbarui atau buat berkas `user_profile.json` di root direktori proyek secara otomatis untuk merekam preferensi baru ini, memastikan sesi penelitian berikutnya lebih cerdas dan selaras dengan pola kerja pengguna.

## Format Output: Integrated Research Dashboard
Di akhir pengerjaan, agen harus menyajikan ringkasan eksekutif satu halaman yang memuat:
1.  **Status Riset**: Ringkasan singkat topik, gap terpilih, dan tujuan utama riset.
2.  **Rangkuman Fase 1-4**: Deskripsi singkat hasil keluaran utama dari masing-masing fase riset yang telah dijalankan secara otomatis.
3.  **Tabel Rekomendasi Publikasi**: Rekomendasi jurnal target terbaik hasil ekstraksi.
4.  **Skor Kelayakan & Masalah Utama**: Hasil evaluasi dari simulasi peer review.
5.  **Daftar Berkas Luaran**: Tautan langsung (file link markdown) ke dokumen detail hasil pengerjaan masing-masing sub-skill (misal: link laporan gap, link desain eksperimen, link tabel matriks, dsb.).
6.  **Pembaruan Memori Personal**: Ringkasan preferensi baru pengguna yang berhasil dipelajari dan disimpan secara implisit ke dalam `user_profile.json`.

## Common Mistakes & Aturan Kritis
- **Lompat Alur (Skipping Flow)**: Mencoba membuat rancangan metode atau mensintesis riset tanpa menyelesaikan penentuan gap dan pertanyaan penelitian (Fase 1) terlebih dahulu.
- **Kehilangan Jejak Output**: Gagal mengirimkan berkas luaran dari skill sebelumnya sebagai input kontekstual ke skill berikutnya, menyebabkan proses riset menjadi tidak konsisten.
- **Mengabaikan Peringatan Kredibilitas**: Tetap melanjutkan ke fase berikutnya meskipun di Fase 3 ditemukan bahwa mayoritas paper rujukan utama tergolong kredibilitas rendah (*low quality*) atau salah sitasi. Agen wajib berhenti dan meminta arahan pengguna untuk merumuskan ulang literatur jika rujukan tidak kredibel.
- **Mengabaikan Pembaruan Profil**: Menyelesaikan riset tanpa memperbarui `user_profile.json` jika ada preferensi penting pengguna yang berubah sepanjang proses penelitian. Jangan mengekspos API Key atau informasi rahasia ke dalam berkas profil ini.
