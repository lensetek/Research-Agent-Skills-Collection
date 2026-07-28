---
name: computer-use
description: >-
  Mengontrol antarmuka GUI desktop dan browser secara otomatis untuk otomasi aplikasi, navigasi visual, serta pengoperasian software pengolah data & statistik (SPSS, EViews, Excel, RapidMiner, Stata, SmartPLS). Menggunakan primary skill stablyai/orca@computer-use dengan mekanisme Auto-Fallback Resilience.
primary_skill: stablyai/orca@computer-use
fallback_references:
  - name: web-infra-dev/midscene-skills@computer-automation
    type: vision-based-ui
    command: npx skills add web-infra-dev/midscene-skills@computer-automation
  - name: am-will/codex-skills@gemini-computer-use
    type: gemini-optimized-schema
    command: npx skills add am-will/codex-skills@gemini-computer-use
---

# Computer Use & GUI Data Software Automation Skill

## Overview
Skill ini memberikan agen kemampuan untuk berinteraksi dengan antarmuka GUI (*Graphical User Interface*) desktop dan browser secara otomatis. Skill ini dikhususkan untuk dua tugas utama:
1. **Otomatisasi Aplikasi Desktop & Browser Umum**: Menavigasi situs web kompleks, mengambil screenshot, mengklik elemen UI, mengisi form, dan menangani dialog sistem.
2. **Otomatisasi Software Pengolah Data & Statistik GUI**: Membuka dan mengendalikan software pengolah data populer seperti **IBM SPSS Statistics**, **EViews**, **Microsoft Excel**, **RapidMiner**, **Stata**, dan **SmartPLS** untuk mengeksekusi uji statistik atau pemodelan ML secara otomatis.

Skill ini dikonfigurasikan dengan **Primary Skill (`stablyai/orca@computer-use`)** dan dilengkapi dengan strategi **Auto-Fallback & Auto-Recovery** apabila terjadi hambatan runtime.

---

## Configuration & Auto-Fallback Resilience

```yaml
primary_skill: stablyai/orca@computer-use
fallback_references:
  - name: web-infra-dev/midscene-skills@computer-automation
    type: vision-based-ui
    command: npx skills add web-infra-dev/midscene-skills@computer-automation
  - name: am-will/codex-skills@gemini-computer-use
    type: gemini-optimized-schema
    command: npx skills add am-will/codex-skills@gemini-computer-use
```

### Cara Kerja Auto-Recovery (Recovery Rules)
1. **Prioritas Eksekusi**: Agen akan selalu mencoba mengeksekusi tindakan menggunakan `stablyai/orca@computer-use` terlebih dahulu.
2. **Kriteria Kegagalan**: Jika eksekusi mengalami kendala (elemen UI tidak responsif, error permission, screenshot terhenti, atau tombol UI kustom tidak dapat diakses):
   - Agen **TIDAK Boleh Langsung Berhenti/Error**.
   - Agen akan membaca daftar `fallback_references` dan mengunduh/memanggil skill fallback secara *on-demand*:
     ```bash
     python "<PATH_KE_SKILL>/scripts/computer_use_runner.py" --action trigger-fallback --fallback-index 0
     ```
   - Agen melanjutkan tugas menggunakan `web-infra-dev/midscene-skills@computer-automation` (Vision-Based AI) atau `am-will/codex-skills@gemini-computer-use`.

---

## Modul Otomatisasi Software Pengolah Data GUI

### 1. IBM SPSS Statistics (.sav, .spv)
- **Membuka Dataset**: Buka aplikasi SPSS -> File -> Open -> Data (`.sav`).
- **Eksekusi Analisis**: Navigasi menu `Analyze`:
  - Regresi Linear: `Analyze -> Regression -> Linear` -> Pilih variabel Dependen & Independen -> Klik OK.
  - ANOVA / T-Test: `Analyze -> Compare Means -> Independent-Samples T Test / One-Way ANOVA`.
  - Uji Validitas/Reliabilitas: `Analyze -> Scale -> Reliability Analysis`.
- **Ekstraksi Hasil**: Tangkap output viewer SPSS, simpan screenshot tabel statistik atau ekspor ke format `.pdf` / `.html` di folder proyek.

### 2. EViews (.wf1, .xlsx)
- **Membuka Workfile**: Buka EViews -> Open EViews Workfile (`.wf1`) atau Import dari Excel.
- **Eksekusi Ekonometrika**:
  - `Quick -> Estimate Equation` -> Masukkan rumus (misal: `Y C X1 X2 X3`).
  - Uji Stasioneritas (Unit Root Test): `View -> Unit Root Test`.
  - Uji Kausalitas Granger: `View -> Granger Causality`.
- **Ekstraksi Hasil**: Tangkap jendela hasil estimasi persamaaan dan simpan angka koefisien, R-squared, t-statistic, dan p-value.

### 3. Microsoft Excel (.xlsx)
- **Spreadsheet Operations**: Buka berkas Excel, baca/tulis sel, buat formula.
- **Data Analysis Toolpak**: Jalankan menu `Data -> Data Analysis` (Regression, ANOVA, Descriptive Statistics).
- **Chart Generation**: Ekstrak atau simpan grafik visualisasi ke format gambar.

### 4. RapidMiner, SmartPLS & Stata
- **RapidMiner**: Buka repositori proses (`.rmp`), jalankan workflow visual ML, ekstrak metrik evaluasi (Accuracy, Precision, Recall, AUC).
- **SmartPLS**: Buka proyek PLS-SEM, jalankan `Calculate -> PLS-SEM Algorithm / Bootstrapping`, tangkap hasil Outer Loadings, R-Square, dan Path Coefficients.
- **Stata**: Jalankan command window Stata atau do-file (`.do`), ambil output regresi panel / time-series.

---

## Workflow Standard

1. **Identifikasi Aplikasi & Target**: Tentukan apakah tugas membutuhkan otomatisasi browser/desktop umum atau otomatisasi software pengolah data GUI (SPSS/EViews/Excel/RapidMiner).
2. **Inisialisasi & Diagnostic Check**: Jalankan pengecekan ketersediaan aplikasi dan layar desktop.
3. **Eksekusi Primary Skill (`stablyai/orca@computer-use`)**: Jalankan instruksi aksi GUI (move mouse, click, write text, screenshot, inspect output).
4. **Auto-Recovery Guardrail**: Jika aksi gagal atau tertahan di elemen UI kustom, panggil fallback `midscene-skills@computer-automation` untuk analisis visual berbasis AI vision.
5. **Ekstraksi & Penyimpanan Hasil**: Simpan hasil tabel, angka statistik, atau screenshot bukti eksekusi ke folder proyek.
