---
name: model-evaluator-validator
description: Bertugas mengevaluasi, memvalidasi, dan menguji signifikansi statistik dari hasil prediksi model komputasi atau Machine Learning untuk memastikan ketangguhan temuan riset.
---

# 🤖 Model Evaluator & Validator

Skill ini memberikan agen kemampuan khusus sebagai spesialis **Quality Assurance & Statistical Validator**. Agen bertugas membedah hasil prediksi dari model yang telah dilatih, mengkritisi performa, dan memastikan bahwa klaim keunggulan model (seperti akurasi tinggi) didukung oleh bukti statistik yang signifikan secara matematis.

## 🎯 Kapan Menggunakan Skill Ini?
- Tepat setelah agen *data-scientist-analyst* selesai memproduksi data hasil prediksi (`predictions.csv` atau sejenisnya).
- Setiap kali riset membutuhkan uji komparatif (misal: "Apakah Model A secara signifikan lebih akurat dari Model B?").
- **Kewajiban**: Agen `research-orchestrator` diwajibkan untuk *selalu* mengeksekusi skill ini pada Fase 2 eksperimen data, tanpa peduli seberapa sederhana modelnya.

## 🛠️ Instruksi Eksekusi

### 1. Inisialisasi dan Pembacaan Data
- Terima berkas *output* mentah dari proses *data-scientist-analyst* yang biasanya berisi kolom nilai Asli (*Ground Truth / y_true*) dan nilai Tebakan (*Prediction / y_pred*).
- Pahami jenis metrik utamanya: Apakah ini klasifikasi (Akurasi, F1, ROC-AUC), regresi (RMSE, MAE, R-Squared), atau prediksi deret waktu/forecasting?

### 2. Pengecekan Baseline (Double Check)
- Tulis *script* Python untuk menghitung ulang metrik standar (seperti RMSE atau Accuracy) guna memastikan tidak ada bias atau manipulasi dari agen pelatih model.
- Bandingkan performa model dengan model *baseline* (seperti model *Naive* atau tebakan mayoritas) jika tersedia.

### 3. Eksekusi Uji Signifikansi Statistik (Wajib)
Berdasarkan jenis data, pilih dan jalankan skrip uji statistik yang tepat menggunakan Python (via `scipy.stats` atau library lainnya):
- **Untuk Regresi / Komparasi Error:** Gunakan **Paired T-Test** (jika terdistribusi normal) atau **Wilcoxon Signed-Rank Test** (non-parametrik) pada deret *Absolute Error* antara dua model.
- **Untuk Klasifikasi:** Gunakan uji **McNemar** untuk menguji signifikansi proporsi perbedaan akurasi antara dua model.
- **Untuk Komparasi ROC-AUC:** Gunakan **DeLong's Test** untuk mengevaluasi apakah dua kurva ROC berbeda secara signifikan.
- **Untuk Deret Waktu (Forecasting):** Gunakan **Diebold-Mariano Test** untuk mengevaluasi perbedaan akurasi prediksi antara dua metode *forecasting*.

### 4. Analisis Residu & Asumsi Model (Khusus Regresi/Ekonometrika)
- Uji Normalitas sisaan (*residuals*) menggunakan **Shapiro-Wilk test**.
- Uji Homoskedastisitas menggunakan **Breusch-Pagan test** atau plot visual.
- Uji Autokorelasi menggunakan **Durbin-Watson test**.

### 5. Format Output (Laporan Validasi Prediksi)
- Buat file laporan (contoh: `validation_report.md`) yang memuat tabel ringkasan nilai *p-value* dari pengujian.
- Interpretasikan hasil pengujian dengan kalimat akademik tegas (misal: "Berdasarkan uji McNemar dengan p-value = 0.012 < 0.05, maka Model A mengungguli Model B secara signifikan.").
- Jelaskan jika terdapat anomali atau kegagalan asumsi (misal heteroskedastisitas tinggi) yang dapat melemahkan klaim karya ilmiah.
- Hasil validasi ini sangat penting dan wajib diserahkan kepada agen penulis di tahap sintesis (Fase 4).
