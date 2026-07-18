---
name: research-orchestrator
description: >-
  Berperan sebagai starter utama yang mengoordinasikan seluruh alur kerja riset secara otomatis dari eksplorasi topik, penentuan gap, metodologi, eksperimen data, sintesis literatur, hingga kesiapan publikasi.
---

# Research Orchestrator (Starter Skill)

## Overview
Skill ini adalah pintu masuk utama (*starter/entry point*) untuk mengotomatiskan seluruh alur kerja riset pada **Research-Agent**. Ketika pengguna mengaktifkan skill ini dengan memberikan ide riset kasar atau domain umum, agen akan mengorkestrasikan dan memanggil 16 skill pendukung lainnya secara berurutan, mengirimkan output dari satu tahap sebagai input ke tahap berikutnya, dan menyajikan laporan akhir berupa *Research Dashboard* terintegrasi.

Secara khusus, skill ini mendukung **Implicit Personalization**. Di awal eksekusi, agen wajib memeriksa keberadaan berkas `user_profile.json` di root direktori untuk memuat preferensi pengguna. Di akhir eksekusi, agen akan menganalisis umpan balik pengguna dan memperbarui berkas tersebut secara otomatis.

## Dependencies
Skill ini mengoordinasikan eksekusi dari 21 skill berikut:
1. `discover-phenomenon-and-gap`
2. `research-question-builder`
3. `hypothesis-or-proposition-builder`
4. `research-design-planner`
5. `synthetic-data-generator`
6. `data-acquisition-specialist`
7. `data-scientist-analyst`
8. `model-evaluator-validator`
9. `literature-review-generator`
10. `extract-methodology`
11. `source-quality-appraiser`
12. `citation-and-reference-validator`
13. `paper-matrix-builder`
14. `synthesize-research`
15. `patent-and-literature-matcher`
16. `journal-recommendation-finder`
17. `journal-template-formatter`
18. `academic-peer-reviewer`
19. `reviewer-response-and-revision`
20. `obsidian-vault-exporter`
21. `agent-update-checker`

## Quick Start
Contoh penggunaan:
*"Gunakan skill research-orchestrator untuk memulai riset otomatis penuh tentang efektivitas metode deteksi penipuan transaksi berbasis grafik (Graph Neural Networks)."*

## Global Directive: Anti-Hallucination & Anti-Mockup
Sebagai Orkestrator, Anda wajib memberlakukan kebijakan "Zero-Tolerance terhadap Data Palsu" pada semua agen bawahan. Setiap kali Anda mendelegasikan tugas kepada agen mana pun, Anda **WAJIB** menyisipkan peringatan berikut di akhir instruksi Anda: 
*"PERINGATAN GLOBAL: Dilarang keras menghasilkan mock data, DataFrame dummy, paper fiktif, atau berhalusinasi. Anda harus memproses data asli dari internet/API. Jika gagal/timeout, laporkan ERROR dan berhenti, jangan pernah mengarang data."*

**Pengecualian Khusus (Whitelisted)**: Agen `synthetic-data-generator` adalah SATU-SATUNYA agen yang diizinkan mengarang data karena tugas spesifiknya adalah membuat persona simulasi (Digital Twin). Jangan mengirimkan peringatan larangan mockup ini kepada agen tersebut.

## Workflow

Agen wajib mengikuti alur eksekusi otomatis 5 fase berikut secara beruntun:

```text
[Cek Update & Baca Profil] ──> [Fase 1: Masalah] ──> [Fase 2: Metodologi & Eksperimen] ──> [Fase 3: Literatur] ──> [Fase 4: Publikasi] ──> [Fase 5: Personalization]
```

### Persiapan Awal (Update Check, Load Profile & Progress Init)
-1. **Pengecekan Pembaruan Terjadwal (Rate-Limited)**: Baca atribut `last_update_check` di dalam `user_profile.json`. Jalankan `agent-update-checker` **hanya jika** pengecekan terakhir dilakukan lebih dari 7 hari yang lalu (atau jika atribut tersebut belum ada). Jika hari ini sudah dicek, abaikan langkah ini agar tidak membuang waktu.
0. Periksa apakah berkas `user_profile.json` ada di root direktori proyek. Jika ada, muat preferensi penelitian.
0b. **Inisialisasi Progress Tracker (WAJIB)**: Jalankan `python bin/progress_tracker.py init --topic "<TOPIC>"` untuk mencatat state 5 fase di `progress.json`. Perbarui state dengan `python bin/progress_tracker.py update` di setiap penyelesaian skill/fase.

### Fase 1: Eksplorasi & Pembingkaian Masalah
1.  Terima topik/ide awal dari pengguna. Tanyakan secara proaktif apakah pengguna ingin mencari ide berbasis literatur teoritis (**Mode A: Literature-Driven**) atau berbasis dataset sekunder (**Mode B: Dataset-Driven (Data Descriptors)**).
2.  Jika pengguna memilih **Mode B**, tanyakan keahlian metodologi/analisis data pilihan mereka (misal: Random Forest, SVM, Regresi Linier, dll.).
3.  Jalankan `discover-phenomenon-and-gap` sesuai mode terpilih:
    - **Mode A**: Petakan fenomena tren terbaru dan rumuskan gap riset ilmiah.
    - **Mode B**: Temukan paper *Data Descriptor* terbaru, ekstrak rekomendasi penulis asli (**Potensi 1**), dan cari usulan inovasi korelasi variabel baru menggunakan metode pilihan pengguna (**Potensi 2**).
    - Presentasikan opsi ide riset ini kepada pengguna, evaluasi indikator "Skala Kesulitan" (Trivial/Moderate/Hardcore), dan minta persetujuan/pilihan pengguna atas opsi yang ingin dieksekusi sebelum melanjutkan ke langkah berikutnya.
4.  Kirimkan ide/gap riset terpilih ke `research-question-builder` untuk merumuskan Pertanyaan Penelitian (RQ), Tujuan, dan Kontribusi riset.
5.  Kirimkan hasil RQ ke `hypothesis-or-proposition-builder` untuk merancang kerangka konseptual teoretis serta hipotesis/proposisi yang akan diuji.

### Fase 2: Perencanaan Metodologi & Eksperimen Data
5.  Kirimkan seluruh dokumen luaran Fase 1 ke `research-design-planner` untuk menyusun detail metodologi eksperimen, penentuan sampling/variabel, alur pengujian data, serta skenario pengujian ketahanan (*robustness/ablation*).
6.  Jalankan `synthetic-data-generator` (jika dibutuhkan) untuk meng-generate dataset sintetis kuantitatif/kualitatif dengan mensimulasikan persona responden.
7.  Jalankan `data-acquisition-specialist` (sebagai opsi/pelengkap) untuk mencari, mengumpulkan, menyedot (*scraping*), atau mengunduh dataset asli dari sumber internet/API.
8.  Jalankan `data-scientist-analyst` untuk melakukan pembersihan data (*preprocessing*), analisis statistik (**WAJIB jalankan `run_stat_analysis.py` dari folder `scripts/` skill terkait**), melatih model Machine Learning, serta memvisualisasikan hasil eksperimen.
9.  Jalankan `model-evaluator-validator` secara wajib untuk melakukan uji signifikansi statistik (misal: T-test, Diebold-Mariano) pada hasil prediksi model guna menguji validitas dan komparasi performanya.

### Fase 3: Kajian & Validasi Literatur
10. Jalankan `literature-review-generator` untuk memetakan perkembangan riset historis dan menyusun argumentasi posisi riset baru. Khusus mode SLR berskala besar, agen wajib mematuhi alur PRISMA 4-tahap (Tarik Metadata -> Filter Python -> Semantic Audit -> Ekstrak) dan menyimpan *checkpoint* `.csv` di tiap langkah.
11. Gunakan `extract-methodology` untuk mengekstrak data teknis dari paper-paper rujukan utama (**WAJIB jalankan `parse_sections.py` dari folder `scripts/` skill terkait** untuk memfilter teks seksi sebelum ekstraksi).
12. Jalankan `source_quality_appraiser` untuk mengaudit tingkat kredibilitas jurnal rujukan (kuartil Scopus/CORE ranking) guna menyaring paper yang lemah metodologinya.
13. Jalankan `citation-and-reference-validator` untuk memverifikasi keakuratan DOI dan memastikan klaim naskah didukung secara faktual. **WAJIB jalankan skrip `validate_references.py` dari folder `scripts/` skill terkait** untuk memfilter referensi palsu sebelum diserahkan ke fase sintesis.
14. Jalankan `paper-matrix-builder` untuk merangkum seluruh parameter teknis rujukan yang telah lolos validasi programatik (**WAJIB jalankan `build_sota_matrix.py` dari folder `scripts/` skill terkait**) ke dalam Tabel State-of-the-Art (SotA) yang terstandarisasi. *(Catatan: Agen wajib mengeksekusi skrip Python menggunakan path absolut lokasi instalasi skill tersebut baik lokal maupun global).*

### Fase 4: Sintesis & Kesiapan Publikasi
15. Jalankan `synthesize-research` untuk menyatukan seluruh bukti temuan literatur, memetakan konsensus, serta mengulas kontradiksi secara kritis.
16. Jalankan `patent-and-literature-matcher` untuk memverifikasi kebaruan (*novelty*) klaim invensi terhadap potensi *prior art*.
17. Jalankan `journal-recommendation-finder` untuk memberikan rekomendasi target jurnal ilmiah (Q1-Q4) yang paling cocok dengan ruang lingkup riset.
18. Jalankan `journal-template-formatter` untuk menstruktur ulang draf akhir sesuai dengan format dan panduan penulisan (*Author Guidelines*) dari jurnal yang dipilih.
19. Jalankan `academic-peer-reviewer` untuk mensimulasikan proses penelaahan sejawat (*peer review*) guna memberikan penilaian kritis, daftar masalah (mayor/minor), serta rekomendasi kelayakan publikasi sebelum dikirim ke jurnal resmi.
20. (Opsional/Jika ada perbaikan) Jalankan `reviewer-response-and-revision` untuk membimbing langkah-langkah revisi naskah.
21. (Opsional/Integrasi Vault) Jalankan `obsidian-vault-exporter` untuk mengekspor dan memformat seluruh dokumen luaran riset ke dalam struktur catatan Obsidian Vault lengkap dengan Frontmatter terstruktur dan *WikiLinks* 2 arah.

### Fase 5: Pembaruan Profil & Memori Riset (Implicit Personalization)
22. Evaluasi seluruh sesi interaksi, komentar, dan umpan balik eksplisit maupun implisit dari pengguna.
23. Perbarui atau buat berkas `user_profile.json` di root direktori proyek secara otomatis untuk merekam preferensi baru ini. Tandai penyelesaian akhir pada `progress.json` dengan `python bin/progress_tracker.py advance`.

## Format Output: Integrated Research Dashboard
Di akhir pengerjaan, agen harus menyajikan ringkasan eksekutif satu halaman yang memuat:
1.  **Status Riset**: Ringkasan singkat topik, gap terpilih, dan tujuan utama riset.
2.  **Rangkuman Fase 1-4**: Deskripsi singkat hasil keluaran utama dari masing-masing fase riset yang telah dijalankan secara otomatis (termasuk hasil dari eksperimen data dan analisis ML).
3.  **Tabel Rekomendasi Publikasi**: Rekomendasi jurnal target terbaik hasil ekstraksi.
4.  **Skor Kelayakan & Masalah Utama**: Hasil evaluasi dari simulasi peer review.
5.  **Daftar Berkas Luaran**: Tautan langsung (file link markdown) ke dokumen detail hasil pengerjaan masing-masing sub-skill (misal: link laporan gap, dataset mentah, script analisis data, dsb.).
6.  **Pembaruan Memori Personal**: Ringkasan preferensi baru pengguna yang berhasil dipelajari dan disimpan secara implisit ke dalam `user_profile.json`.

## Common Mistakes & Aturan Kritis
- **Lompat Alur (Skipping Flow)**: Mencoba membuat rancangan metode atau mensintesis riset tanpa menyelesaikan penentuan gap dan pertanyaan penelitian (Fase 1) terlebih dahulu.
- **Kehilangan Jejak Output**: Gagal mengirimkan berkas luaran dari skill sebelumnya sebagai input kontekstual ke skill berikutnya, menyebabkan proses riset menjadi tidak konsisten.
- **Mengabaikan Peringatan Kredibilitas**: Tetap melanjutkan ke fase berikutnya meskipun di Fase 3 ditemukan bahwa mayoritas paper rujukan utama tergolong kredibilitas rendah (*low quality*) atau salah sitasi. Agen wajib berhenti dan meminta arahan pengguna untuk merumuskan ulang literatur jika rujukan tidak kredibel.
- **Mengabaikan Pembaruan Profil**: Menyelesaikan riset tanpa memperbarui `user_profile.json` jika ada preferensi penting pengguna yang berubah sepanjang proses penelitian. Jangan mengekspos API Key atau informasi rahasia ke dalam berkas profil ini.
