---
name: project-setup-git
description: Skill untuk melakukan setup proyek melalui git clone/pull alih-alih menggunakan npx (Mendukung pedoman keamanan kredensial dan desain mobile-view first).
---

# Project Setup via Git (Clone/Pull)

## Overview
Skill ini digunakan ketika pengguna meminta untuk melakukan setup atau inisialisasi proyek menggunakan Git (`git clone` atau `git pull`) alih-alih membuat proyek baru menggunakan perintah `npx`. Skill ini memandu agen untuk mengunduh basis kode yang ada, menginstal dependensi yang sesuai, melakukan konfigurasi dasar dengan aman, serta menjalankan proyek dengan tampilan responsif.

## Dependencies
- Tidak ada

## Quick Start
Contoh penggunaan:
*"Gunakan skill project-setup-git untuk mengkloning repositori https://github.com/example/repo ke direktori kerja dan instal seluruh dependensinya."*

## Workflow

### 1. Kloning atau Pembaruan Repositori (Clone/Pull)
- Gunakan perintah `git clone <url_repositori> .` untuk mengkloning basis kode yang sudah ada ke dalam direktori kerja saat ini.
- Jika direktori tersebut sudah merupakan repositori Git aktif, gunakan perintah `git pull` untuk mengambil (*fetch*) dan menggabungkan (*merge*) perubahan terbaru.

### 2. Deteksi & Instalasi Dependensi
- Periksa file *lockfile* yang ada di root direktori untuk mendeteksi *package manager* yang digunakan:
  - Jika ada `package-lock.json`, jalankan `npm install`.
  - Jika ada `yarn.lock`, jalankan `yarn install`.
  - Jika ada `pnpm-lock.yaml`, jalankan `pnpm install`.

### 3. Konfigurasi Lingkungan (Environment Setup)
- Salin file lingkungan contoh (misalnya, `cp .env.example .env` atau perintah salin yang sesuai di PowerShell/CMD).
- Minta pengguna untuk mengonfigurasi variabel lingkungan yang dibutuhkan secara manual.

### 4. Eksekusi Proyek
- Mulai server pengembangan (*development server*) menggunakan perintah `npm run dev` atau perintah start yang sesuai dengan konfigurasi proyek.

## Common Mistakes & Aturan Kritis
- **Eksposur Kredensial Sensitif**: DILARANG keras membiarkan kredensial proyek (seperti API key, password, token) terekspos secara publik di frontend atau diakses melalui client-side. Selalu cek keamanan file `.env` dan pastikan dimasukkan ke dalam `.gitignore`.
- **Mengabaikan Tampilan Responsif**: Mengabaikan pendekatan *mobile-view first* saat melakukan kustomisasi UI/layout pasca-setup. Antarmuka harus selalu dirancang responsif sejak awal.
- **Salah Mendeteksi Package Manager**: Menjalankan `npm install` pada proyek yang memiliki `yarn.lock` atau `pnpm-lock.yaml`, yang dapat merusak konsistensi dependensi proyek.
- **Penggunaan cd Command**: Jangan gunakan perintah `cd` untuk berpindah direktori di terminal dalam command line yang diajukan ke pengguna; jalankan perintah langsung pada *current working directory* (Cwd) yang sesuai di konfigurasi tool run_command.
