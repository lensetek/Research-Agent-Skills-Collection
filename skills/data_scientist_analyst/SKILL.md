---
name: data-scientist-analyst
description: >-
  Bertugas memproses, menganalisis, menguji statistik, melatih model Machine Learning, dan membuat visualisasi data ilmiah secara terstruktur.
---

# Data Scientist Analyst

## Overview
Skill ini bertanggung jawab untuk mengubah data mentah hasil akuisisi menjadi wawasan (*insights*) ilmiah yang kredibel. Agen akan menulis script Python untuk melakukan pembersihan data (*preprocessing*), uji statistik inferensial (regresi, PLS, ANOVA), pemodelan prediktif (*Machine Learning*), serta memvisualisasikan hasil metrik performa secara profesional (Matplotlib/Seaborn).

## Dependencies
- Menggunakan library Python standar dan pihak ketiga untuk analisis data dan machine learning (Pandas, NumPy, SciPy, Statsmodels, Scikit-Learn, Matplotlib, Seaborn, XGBoost, LightGBM, dll.).
- Agen dapat menginstal dependensi Python secara terprogram via terminal.

## Quick Start
Contoh penggunaan:
*"Gunakan skill data-scientist-analyst untuk melakukan analisis regresi PLS pada dataset saham_bank.csv dan tampilkan visualisasi feature importance."*

## Data Analysis & Machine Learning Rules (ATURAN MUTLAK)
1. **Rigorous Data Preprocessing**: Selalu periksa nilai kosong (*missing values*), pencilan (*outliers*), dan lakukan standardisasi/normalisasi fitur sebelum melatih model ML.
2. **Methodological Statistics**:
   - Untuk analisis hubungan variabel: Lakukan uji regresi linear/logistik berganda atau *Partial Least Squares* (PLS).
   - Selalu sertakan nilai statistik penting seperti p-value, R-squared, t-statistic, dan F-statistic untuk memvalidasi signifikansi.
3. **Machine Learning Best Practices**:
   - Lakukan pembagian dataset (*train-test split*) secara ketat untuk menghindari kebocoran data (*data leakage*).
   - Gunakan *cross-validation* (misal: K-Fold) untuk mengukur ketahanan model.
   - Bandingkan minimal dua algoritma model berbeda (misal: Linear Regression vs Random Forest) untuk menunjukkan perbandingan performa.
4. **Professional Visualization**:
   - Semua plot/grafik yang dihasilkan wajib memiliki label sumbu X dan Y, legenda, judul, serta menggunakan skema warna yang elegan (misal: palet *seaborn-v0_8* atau *coolwarm*).
   - Simpan visualisasi hasil ke dalam format `.png` atau `.pdf` berkualitas tinggi di direktori proyek.

## Workflow Execution
1. **Muat Dataset**: Baca berkas data mentah yang ada di proyek (seperti `.csv`, `.json`, atau `.xlsx`).
2. **Eksekusi Analisis Statistik Deterministik (WAJIB)**: Sebelum menulis analisis kustom, jalankan skrip pembantu statistik untuk menghasilkan ringkasan angka faktual tanpa risiko halusinasi *(Gunakan path absolut dari `run_stat_analysis.py` di direktori instalasi skill ini)*:
  ```bash
  python "<PATH_KE_SKILL>/scripts/run_stat_analysis.py" --input dataset.csv --output stat_report.json
  ```
3. **Hardware Workload Pre-flight Check (Rekomendasi untuk Training Dataset Besar)**: Sebelum melatih model ML berat / deep learning, gunakan skill `hardware-workload-estimator` untuk memeriksa CPU, System RAM, dan VRAM GPU lokal. Jika estimasi waktu > 20 menit atau berisiko OOM, tawarkan migrasi eksekusi ke **Google Colab** via Chrome DevTools MCP.
4. **Eksplorasi Data (EDA)**: Gunakan angka pasti dari `stat_report.json` untuk menganalisis karakteristik dataset (mean, std, median, null count).
5. **Penyusunan Script Analisis & Pemodelan Data (3-Tier Execution Hierarchy)**: 
   - **Tier 1 (Python Native Stack - REKOMENDASI UTAMA)**: Gunakan Python (`pandas`, `statsmodels`, `scipy`, `pyreadstat`, `scikit-learn`). Python mampu membaca file SPSS (`.sav`), Stata (`.dta`), dan Excel (`.xlsx`) secara *native* dan memberikan perhitungan statistik yang 100% akurat tanpa lisensi software komersial.
   - **Tier 2 (Headless Batch Mode - SPSS/EViews/Stata/Excel)**: Jika pengguna mewajibkan software spesifik, panggil skill `computer-use` untuk mengeksekusi script batch (`.sps`, `.prg`, `.do`) di background via CLI.
   - **Tier 3 (GUI Computer-Use Vision Fallback)**: Digunakan jika butuh simulasi navigasi antarmuka visual interaktif.
6. **Eksekusi & Evaluasi**: Jalankan skrip analisis tersebut, evaluasi metrik performa (R2, F1-Score, RMSE, p-value), dan pastikan bebas error.
7. **Interpretasi Riset & Visualisasi**: Sajikan kesimpulan akademik berupa narasi ilmiah yang menjelaskan makna fungsional dari angka-angka hasil pemodelan, dan berikan tautan langsung ke berkas grafik visualisasi yang disimpan.

## Common Mistakes
- **Data Leakage**: Melakukan proses scaling/normalisasi pada keseluruhan dataset sebelum membaginya menjadi data train dan test.
- **Overfitting**: Melaporkan akurasi latih yang tinggi tanpa memverifikasi performa model pada data pengujian independen.
- **Uji Statistik Tanpa Asumsi**: Melakukan uji parametrik (seperti T-Test atau ANOVA) tanpa terlebih dahulu memverifikasi asumsi normalitas data.
