---
name: hardware-workload-estimator
description: >-
  Mengecek spesifikasi perangkat komputasi lokal pengguna (CPU, RAM, GPU VRAM), mengestimasi beban kerja & durasi training dataset/uji statistik, memberikan rekomendasi lokal vs Google Colab, serta mengotomatisasi Google Colab via Chrome DevTools MCP.
---

# Hardware Workload Estimator & Cloud Advisor

## Overview
Skill ini berfungsi sebagai inspektur komputasi dan konsultan alokasi beban kerja (*workload manager*). Sebelum mengeksekusi *Machine Learning model training*, pemrosesan dataset besar, atau uji statistik inferensial intensif, agen akan memeriksa kemampuan perangkat keras lokal (CPU, System RAM, GPU/VRAM) dan memperkirakan risiko *Out-Of-Memory (OOM)* atau durasi training yang terlalu lama.

Jika eksekusi di lokal diperkirakan tidak efisien atau berisiko gagal, agen akan merekomendasikan dan membantu migrasi eksekusi ke **Google Colab** (atau platform cloud lain) dengan memanfaatkan integrasi **Chrome DevTools MCP** secara otomatis.

---

## Aturan Keamanan & Privasi Data (ATURAN MUTLAK)

> [!CAUTION]
> **Kebocoran Kredensial & Data Sensitif**: Sebelum merekomendasikan atau mengunggah dataset/kode ke Google Colab atau cloud provider publik, agen WAJIB melakukan pemindaian otomatis untuk memastikan **TIDAK ADA** API Key, password, token otentikasi, atau data pribadi (PII) di dalam dataset atau skrip. Jika ditemukan data sensitif, lakukan anonisasi atau peringatkan pengguna secara eksplisit.

---

## Standard Workflow

### Step 1: Pre-Flight Hardware Inspection
Jalankan skrip diagnostik perangkat keras lokal untuk mendapatkan informasi terstruktur mengenai CPU, RAM, dan ketersediaan GPU (CUDA/MPS/DirectML):

```bash
python "<PATH_KE_SKILL>/scripts/check_hardware.py"
```

Output berupa JSON berisi ketersediaan VRAM, jumlah core CPU, serta ketersediaan memori RAM sistem.

---

### Step 2: Workload Estimation & Micro Dry-Run
Lakukan pengukuran throughput awal dengan menjalankan 1-2 batch kecil pada 1% sampel dataset (micro dry-run). Kemudian jalankan kalkulasi estimasi:

```bash
python "<PATH_KE_SKILL>/scripts/estimate_workload.py" --total-samples <TOTAL> --batch-size <BATCH> --epochs <EPOCHS> --sample-time-sec <TIME_PER_BATCH> --sample-vram-mb <VRAM_PER_BATCH> --available-vram-gb <VRAM_LOKAL> --available-ram-gb <RAM_LOKAL>
```

Skrip ini akan memisahkan keputusan:
* `RECOMMENDED_LOCAL`: Jika estimasi durasi $< 20$ menit dan estimasi penggunaan VRAM $< 85\%$ kapasitas maksimum.
* `RECOMMENDED_CLOUD_COLAB`: Jika estimasi durasi $> 20$ menit atau terdapat risiko tinggi Out-Of-Memory (OOM).

---

### Step 3: Present Recommendation Matrix to User
Tampilkan matriks rekomendasi transparan kepada pengguna dengan format:

| Parameter Komputasi | Spesifikasi / Estimasi Lokal | Status / Catatan |
| :--- | :--- | :--- |
| **GPU / Accelerator** | NVIDIA RTX / Apple MPS / CPU | status ketersediaan CUDA |
| **Tersedia RAM / VRAM** | XX GB RAM / YY GB VRAM | kecukupan kapasitas memori |
| **Proyeksi Waktu Training** | $\approx$ XX Menit | lokal vs cloud threshold |
| **Rekomendasi Utama** | **EKSEKUSI LOKAL** / **MIGRASI GOOGLE COLAB** | rekomendasi final |

---

### Step 4: Automated Google Colab Offloading (via Chrome DevTools MCP)
Jika pengguna menyetujui rekomendasi Google Colab:
1. **Generate Notebook**: Buat berkas `.ipynb` Colab-ready menggunakan skrip:
   ```bash
   python "<PATH_KE_SKILL>/scripts/generate_colab_notebook.py" --script "<TRAINING_SCRIPT.py>" --output "colab_training_notebook.ipynb"
   ```
2. **Chrome DevTools MCP Automation**:
   - Gunakan fitur Chrome DevTools / Browser control yang tersemat untuk membuka `https://colab.research.google.com/`.
   - Unggah berkas `colab_training_notebook.ipynb` atau buat notebook baru.
   - Atur runtime accelerator ke **GPU (T4/V100/A100)**.
   - Eksekusi cell pertama (instalasi & verifikasi GPU).

---

### Step 5: Local Downscaling Option (Jika Pengguna Memilih Tetap Lokal)
Jika pengguna menolak cloud dan memilih tetap di lokal:
* Gunakan **Mixed Precision (`FP16`/`BF16`)**.
* Kurangi `batch_size` dan terapkan **Gradient Accumulation**.
* Lakukan *subsampling* dataset untuk pengujian statistik preliminary sebelum full run.

---

### Step 6: Generate & Update HITL Research Checklist
Setelah memberikan rekomendasi dan menyiapkan lingkungan eksekusi, perbarui berkas kendali pengguna `hitl_research_checklist.md` (menggunakan skrip `skills/research_orchestrator/scripts/generate_hitl_checklist.py`) agar pengguna dapat memeriksa dan menandatangani persetujuan eksekusi (*Human-in-the-Loop Sign-Off*).
