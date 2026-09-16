---
name: agent-update-checker
description: >-
  Bertugas untuk mengecek pembaruan (update) agent skills terbaru dari repositori GitHub serta memeriksa dan memperbarui paket otomatisasi Chrome DevTools MCP & Windows MCP (cursortouch/windows-mcp) secara terintegrasi.
---

# Agent Update Checker & Multi-MCP Auto-Updater

## Overview
Skill ini bertugas sebagai sistem pemeliharaan (*maintenance*) terpusat untuk memastikan bahwa seluruh kumpulan skill **Research-Agent** serta dependensi MCP kunci (**Chrome DevTools MCP** dan **Windows MCP**) selalu berada dalam versi terbaru dan siap pakai tanpa risiko error *"package not installed"*.

## Dependencies
- Skrip pembantu Python: `bin/mcp_auto_updater.py` (untuk memeriksa & menginstal 3 entitas secara otomatis).

## Quick Start
Contoh penggunaan:
> *"Gunakan skill agent-update-checker untuk mengecek apakah ada versi terbaru dari agent skills, Chrome DevTools MCP, dan Windows MCP."*

---

## Workflow

### 1. Eksekusi Pengecekan Terintegrasi (3-Entity Check)
Agen mengeksekusi skrip pemeriksaan terpadu melalui terminal:
```bash
py bin/mcp_auto_updater.py --check --json
```
Skrip ini akan memeriksa 3 entitas secara simultan:
1. **Research-Agent-Skills-Collection:** Repositori skill utama di GitHub (`https://github.com/lensetek/Research-Agent-Skills-Collection`).
2. **Chrome DevTools MCP (`chrome-devtools-mcp`):** Memeriksa ketersediaan paket `npx -y chrome-devtools-mcp@latest`.
3. **Windows MCP (`cursortouch/windows-mcp`):** Memeriksa ketersediaan paket `uvx windows-mcp` / `pip install windows-mcp` di OS Windows.

### 2. Pelaporan & Konfirmasi ke Pengguna
- Berikan laporan ringkas mengenai status ketiga paket tersebut kepada pengguna:
  > *"Hasil Pengecekan Pembaruan:*  
  > *1. Agent Skills Repo: Terdapat commit/fitur baru.*  
  > *2. Chrome DevTools MCP: Siap dipicu via npx -y chrome-devtools-mcp@latest.*  
  > *3. Windows MCP: Siap dipicu via uvx windows-mcp serve.*"
- Tanyakan secara eksplisit kepada pengguna: **"Apakah Anda ingin saya mengunduh dan memperbarui seluruh versi agent skill dan paket MCP ke versi paling mutakhir?"**

### 3. Eksekusi Pembaruan Terpadu (Jika Disetujui)
Jika pengguna menjawab "Ya" atau menyetujui pembaruan:
1. **Update MCP Dependencies:**
   ```bash
   py bin/mcp_auto_updater.py --update
   ```
2. **Update Agent Skills Collection:**
   Agen meminta pengguna atau mengeksekusi pengunduhan ulang dari URL repositori utama:
   > *"Tolong download dan install update agent skill dari url https://github.com/lensetek/Research-Agent-Skills-Collection"*

---

## Common Mistakes & Aturan Kritis
- **Overwrite Tanpa Izin**: Dilarang keras menimpa (*overwrite*) atau mengunduh pembaruan tanpa ada konfirmasi "Ya" dari pengguna. Selalu tanyakan dulu.
- **Menghapus Konfigurasi Personal**: Pembaruan ini DILARANG me-reset berkas personalisasi seperti `user_profile.json` atau kredensial rahasia di `.env`.
- **Menyatakan Package Not Installed**: DILARANG menyatakan paket `chrome-devtools-mcp` atau `windows-mcp` tidak terinstall; selalu jalankan auto-provisioning via `bin/mcp_auto_updater.py`.
