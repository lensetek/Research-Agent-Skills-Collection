---
name: journal-template-formatter
description: >-
  Bertugas mengubah, menyusun, dan memformat draf makalah riset menjadi format jurnal penelitian sesuai dengan panduan penulis (Author Guidelines) atau template yang dituju (misal IEEE, APA, Elsevier).
---

# Journal Template Formatter

## Overview
Skill ini dirancang untuk memandu Research Agent dalam mengubah, menyusun, dan memformat draf makalah riset agar sepenuhnya mematuhi pedoman penulisan (*Author Guidelines*) dari jurnal atau penerbit target (seperti IEEE, APA, Nature, Elsevier, dll.). Agen berfokus pada penataan struktur bab, format afiliasi, penyesuaian gaya selingkung bahasa, serta perapian sitasi dan daftar pustaka tanpa mengubah substansi ilmiah naskah asli.

## Dependencies
- `citation-and-reference-validator`
- `markdown-to-latex-converter`

## Quick Start
Contoh penggunaan:
*"Gunakan skill journal-template-formatter untuk menyesuaikan struktur dan format daftar pustaka draf artikel riset ini ke format jurnal IEEE Transactions."*

## Workflow

### 1. Identifikasi Kebutuhan & Spesifikasi Jurnal
- Identifikasi jurnal target atau gaya format yang diinginkan pengguna (misal: APA 7th Edition, IEEE, Harvard, Nature, Elsevier).
- Jika pengguna tidak menentukan jurnal target atau pedoman tertentu secara spesifik, tawarkan format standar akademik (struktur IMRAD dengan gaya sitasi APA).

### 2. Analisis Struktur Draf & Deteksi Komponen
- Lakukan analisis terhadap draf artikel riset masukan untuk memahami isinya.
- Periksa kelengkapan komponen wajib dasar seperti Judul, Abstrak, Pendahuluan, Metode, Hasil, Diskusi, Kesimpulan, dan Daftar Pustaka.

### 3. Pemformatan, Restrukturisasi & Penyesuaian Gaya Selingkung
- Ubah urutan bab dan sub-bab sesuai dengan *template* atau struktur baku jurnal target.
- Sesuaikan format afiliasi penulis, batas kata untuk abstrak, kata kunci (*keywords*), dan gaya bahasa (selingkung/gaya penulisan akademis).
- Rapikan format sitasi dalam teks (*in-text citation*) dan entri daftar pustaka (*references*) agar konsisten dan sesuai dengan panduan jurnal target.

### 4. Pengecekan Komponen Tambahan (Missing Sections Check)
- Identifikasi bagian opsional/wajib tambahan yang biasanya diminta oleh penerbit (seperti *Conflict of Interest*, *Acknowledgment*, *Author Contributions*, *Funding Information*).
- Berikan peringatan atau catatan kepada pengguna jika komponen ini belum ada dalam draf asli agar pengguna dapat melengkapinya.

### 5. Penyusunan Output & Delegasi Format
- Sajikan naskah hasil pemformatan akhir yang bersih, rapi, dan siap dipublikasikan.
- Jika pengguna meminta atau membutuhkan keluaran dalam bentuk LaTeX, delegasikan proses konversi dokumen Markdown ke LaTeX menggunakan skill `markdown-to-latex-converter`.

## Common Mistakes & Aturan Kritis
- **Mengubah Konten Ilmiah**: DILARANG keras memodifikasi data eksperimen, hasil analisis, tabel data, gambar, makna kalimat, atau klaim ilmiah utama dari naskah asli. Pemformatan hanya fokus pada tata letak, struktur, dan gaya sitasi.
- **Perubahan Tanpa Transparansi**: Melakukan penyuntingan bahasa (copyediting) atau penyempurnaan kalimat tanpa menunjukkannya kepada pengguna secara jelas. Perubahan bahasa minor diperbolehkan untuk keselarasan akademis, namun substansi harus dipertahankan secara utuh.
- **Format Sitasi Tidak Konsisten**: Mencampuradukkan gaya sitasi (misal, sebagian memakai angka gaya IEEE dan sebagian memakai nama-tahun gaya APA) dalam satu naskah. Semua sitasi wajib dirapikan secara seragam.
- **Mengabaikan Pedoman Batas Kata**: Membiarkan abstrak atau konten utama melebihi batas jumlah kata yang telah ditentukan dalam Author Guidelines jurnal target.
