---
name: project-setup-git
description: Skill for setting up a project via git clone/pull instead of npx (English & Bahasa Indonesia).
---

# Project Setup via Git (Clone/Pull)
# Setup Proyek melalui Git (Clone/Pull)

## English Instructions
When a user asks to set up or initialize a project without using `npx`, follow these steps:
1. **Clone or Pull**: Use `git clone <repository_url> .` to clone the existing codebase into the current directory. If the directory is already a git repository, use `git pull` to fetch and merge the latest changes.
2. **Install Dependencies**: Check for existing lockfiles to determine the package manager. Run `npm install`, `yarn install`, or `pnpm install` depending on whether `package-lock.json`, `yarn.lock`, or `pnpm-lock.yaml` is present.
3. **Configuration**: Copy the example environment file (e.g., `cp .env.example .env`) and ask the user to configure it. 
   - **CRITICAL SECURITY RULE**: Never expose sensitive project credentials to the public. Ensure credentials are secure and cannot be accessed via client-side frontend code.
4. **Run the Project**: Start the development server using `npm run dev` or the appropriate start command.
5. **Design Guidelines**: Ensure any UI development strictly follows a mobile-first responsive design approach.

## Instruksi Bahasa Indonesia
Ketika pengguna meminta untuk melakukan setup atau inisialisasi proyek tanpa menggunakan `npx`, ikuti langkah-langkah berikut:
1. **Clone atau Pull**: Gunakan perintah `git clone <url_repositori> .` untuk mengkloning basis kode yang sudah ada ke dalam direktori saat ini. Jika direktori tersebut sudah merupakan repositori git, gunakan `git pull` untuk mengambil dan menggabungkan perubahan terbaru.
2. **Instal Dependensi**: Periksa file lock yang ada untuk menentukan package manager yang digunakan. Jalankan `npm install`, `yarn install`, atau `pnpm install` tergantung pada ketersediaan file `package-lock.json`, `yarn.lock`, atau `pnpm-lock.yaml`.
3. **Konfigurasi**: Salin file environment contoh (misalnya, `cp .env.example .env`) dan minta pengguna untuk mengonfigurasinya.
   - **ATURAN KEAMANAN KRITIS**: Selalu cek keamanan credential project agar tidak terekspose ke publik atau dapat diakses melalui client-side di frontend.
4. **Jalankan Proyek**: Mulai server pengembangan menggunakan perintah `npm run dev` atau perintah start yang sesuai.
5. **Panduan Desain**: Selalu perhatikan tampilan desain antarmuka (UI) agar responsif dengan pendekatan mobile-view first.
