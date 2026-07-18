---
name: citation-and-reference-validator
description: >-
  Memvalidasi kebenaran metadata referensi (DOI, tautan, judul, penulis, tahun) dan keselarasan kontekstual antara kalimat klaim di naskah dengan konten paper yang dirujuk.
---

# Citation & Reference Validator

## Overview
Skill ini dirancang untuk melakukan audit kualitas terhadap kutipan (*citations*) dan daftar pustaka (*references*) dalam sebuah naskah ilmiah. Agen memastikan bahwa semua rujukan memiliki metadata yang valid (bebas dari referensi palsu hasil halusinasi AI) dan bahwa teks kalimat rujukan dalam naskah benar-benar didukung secara faktual oleh paper yang disitasi (*contextual alignment*).

## Dependencies
- `literature-search-openalex`
- `pubmed-database`

## Quick Start
Contoh penggunaan:
*"Gunakan skill citation-and-reference-validator untuk mengecek apakah kalimat klaim 'Metode X memiliki akurasi 98% (Smith et al., 2022)' benar-benar didukung oleh isi paper Smith et al. dengan DOI 10.1000/xyz."*

## Workflow

### 1. Validasi Metadata Referensi (Programmatic Metadata Integrity Audit)
- **Eksekusi Guardrail Programatik (WAJIB)**: Sebelum melakukan penilaian manual, agen **WAJIB** mengeksekusi skrip verifikasi otomatis untuk memvalidasi daftar pustaka terhadap API Crossref dan OpenAlex. 
  *(Catatan: Tentukan path absolut dari `validate_references.py` berdasarkan lokasi direktori `SKILL.md` ini berada, baik instalasi lokal maupun global)*:
  ```bash
  python "<PATH_KE_SKILL>/scripts/validate_references.py" --input references.json --output report.json
  ```
  atau jalankan secara langsung untuk single DOI/Title:
  ```bash
  python "<PATH_KE_SKILL>/scripts/validate_references.py" --doi <DOI> --title "<TITLE>"
  ```
- Evaluasi luaran `report.json`:
  - **`VALID`**: Metadata terverifikasi resmi oleh database publik (Crossref/OpenAlex).
  - **`METADATA_MISMATCH`**: Paper ditemukan, namun atribut tahun/penulis/judul yang diberikan berbeda signifikan dari database asli.
  - **`HALLUCINATED`**: DOI atau judul tidak ditemukan di basis data publik manapun. **Wajib langsung ditolak / dibuang dari daftar rujukan.**
- Tandai referensi yang berstatus `HALLUCINATED` atau `METADATA_MISMATCH` secara eksplisit pada laporan audit.

### 2. Validasi Keselarasan Konteks Kutipan (Contextual Citation Alignment)
- Ambil kalimat di naskah yang berisi sitasi (misal: *"Model transformer terbukti tidak stabil pada sekuens panjang [1]"*).
- Baca isi abstrak atau bagian metodologi/hasil dari paper referensi target [1].
- Analisis apakah kesimpulan atau data pada paper [1] benar-benar mendukung pernyataan tersebut, atau apakah ada penyimpangan pemahaman (salah interpretasi).
- Klasifikasikan status dukungan:
  - **Didukung Penuh (Fully Supported)**: Klaim naskah selaras dengan hasil/pernyataan langsung di paper rujukan.
  - **Didukung Sebagian (Partially Supported)**: Klaim naskah memerlukan modifikasi karena paper rujukan memberikan batasan atau konteks tertentu yang tidak disebutkan di naskah.
  - **Tidak Didukung / Kontradiktif (Unsupported/Contradictory)**: Paper rujukan tidak membahas isu tersebut atau justru menghasilkan kesimpulan yang bertentangan.
  - **Salah Sitasi (Misattribution)**: Paper rujukan membahas topik yang berbeda sama sekali.

### 3. Pengecekan Gaya Sitasi & Konsistensi (Format Check)
- Pastikan penulisan sitasi konsisten mengikuti pedoman penulisan tertentu (e.g., APA, IEEE, Harvard, MLA) baik di dalam teks maupun di daftar pustaka.
- Pastikan semua dokumen yang disitasi di dalam teks tercantum di daftar pustaka, dan sebaliknya.

### 4. Format Laporan Validasi Rujukan
Sajikan laporan audit rujukan dalam format tabel wajib berikut:
| Teks Kalimat / Klaim Naskah | Paper Rujukan (Sitasi) | Validitas Metadata & DOI | Status Dukungan Kontekstual | Catatan Perbaikan |
|---|---|---|---|---|

## Common Mistakes & Aturan Kritis (Anti-Halusinasi Referensi)
- **Referensi Halusinasi (Fake References)**: Menyertakan rujukan buatan AI yang terlihat meyakinkan (memiliki nama penulis terkenal dan judul yang masuk akal) namun sebenarnya tidak pernah dipublikasikan atau DOI-nya palsu.
- **Kutipan Berantai yang Menyesatkan (Lazy Citation)**: Mengutip paper B yang mengutip paper A untuk suatu teori, padahal isi asli paper A berbeda dengan interpretasi paper B. Agen wajib menelusuri sumber primer jika kemungkinan akses PDF/Teks penuh terbuka tersedia.
- **Overgeneralization Citation**: Mengutip paper eksperimen spesifik seolah-olah itu membuktikan teori universal tanpa menyebutkan batasan uji eksperimen dari paper tersebut.
- **Salah Format Penulisan**: Tidak konsisten dalam menyusun daftar referensi (menggabungkan format APA dan IEEE secara acak).
- **Hambatan API Key**: Menghentikan proses audit atau memunculkan pesan error ketika API Key Semantic Scholar tidak terisi. Lakukan validasi silang menggunakan API publik gratis (OpenAlex / Crossref) yang tidak membatasi akses tanpa token.
