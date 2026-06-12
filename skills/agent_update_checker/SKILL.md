---
name: agent-update-checker
description: >-
  Bertugas untuk mengecek pembaruan (update) agent skills terbaru dari repositori GitHub dan mengonfirmasi pengguna apakah ingin mengunduh versi terbaru.
---

# Agent Update Checker

## Overview
Skill ini bertugas sebagai sistem pemeliharaan (maintenance) untuk memastikan bahwa pengguna selalu memiliki versi kumpulan skill **Research-Agent** yang paling mutakhir. Skill ini dapat dipanggil secara manual melalui prompt untuk mengecek adanya versi terbaru di repositori resmi GitHub.

## Dependencies
Tidak ada dependensi khusus. Agen dapat membaca URL secara langsung.

## Quick Start
Contoh penggunaan:
*"Gunakan skill agent-update-checker untuk mengecek apakah ada versi terbaru dari kumpulan skill agen ini."*

## Workflow

### 1. Pengecekan Versi Terbaru
- Agen mengakses URL repositori resmi: `https://github.com/lensetek/Research-Agent-Skills-Collection`.
- Analisis bagian utama repositori (seperti riwayat *commit* terakhir, atau teks *What's New* di README.md) untuk melihat apakah ada perubahan baru dibandingkan yang saat ini dimiliki pengguna.

### 2. Konfirmasi ke Pengguna
- Berikan laporan singkat kepada pengguna: *"Saat ini terdapat pembaruan baru di repositori utama..."* beserta rincian singkat fitur apa yang baru.
- Tanyakan secara eksplisit kepada pengguna: **"Apakah Anda ingin saya mengunduh dan memperbarui versi agent skill Anda ke versi terbaru ini?"**

### 3. Eksekusi Pembaruan (Jika Disetujui)
- Jika pengguna menjawab "Ya" atau setuju, jalankan proses instalasi/pembaruan sederhana dengan cara meminta pengguna memicu prompt instalasi ulang dari URL, atau agen langsung memproses pengunduhan ulang.
- Prompt instruksi pengunduhan standar:
  > *"Tolong download dan install update agent skill dari url https://github.com/lensetek/Research-Agent-Skills-Collection"*

## Common Mistakes & Aturan Kritis
- **Overwrite Tanpa Izin**: Dilarang keras menimpa (overwrite) atau mengunduh pembaruan tanpa ada konfirmasi "Ya" dari pengguna. Selalu tanyakan dulu.
- **Menghapus Konfigurasi Personal**: Ingatkan pengguna (atau pastikan sistem agen) bahwa pembaruan ini tidak boleh menghapus atau me-reset berkas personalisasi seperti `user_profile.json` atau kredensial rahasia di `.env`.
