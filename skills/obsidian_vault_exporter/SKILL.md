---
name: obsidian-vault-exporter
description: >-
  Bertugas mentransformasikan, merestrukturisasi, dan mengekspor seluruh hasil riset (abstrak, literature review, matriks komparasi, hipotesis) menjadi berkas Markdown Obsidian-native lengkap dengan YAML Frontmatter terstruktur, bidirectional links ([[WikiLinks]]), tag, serta query Dataview siap pakai.
---

# Obsidian Vault Exporter

## Overview
Skill ini dirancang untuk memandu Research Agent dalam mengonversi dan mentransformasikan seluruh dokumen hasil riset (literature notes, matriks perbandingan paper, sintesis riset, hipotesis, dan rekomendasi jurnal) menjadi catatan interaktif yang siap dimasukkan ke dalam **Obsidian Vault** (*Second Brain*). Agen secara otomatis menyusun YAML Frontmatter terstruktur, menambahkan *bidirectional WikiLinks* (`[[Note Name]]`), menandai tag kustom, serta menyajikan skrip *Dataview Query* untuk membangun *Knowledge Graph* riset yang kaya dan mudah dicari.

## Dependencies
- `extract-methodology`
- `paper-matrix-builder`
- `synthesize-research`

## Quick Start
Contoh penggunaan:
*"Format seluruh hasil literature review dan matriks paper ini ke dalam struktur Obsidian Vault lengkap dengan Frontmatter, WikiLinks antar-paper, dan query Dataview."*

## Workflow

### 1. Deteksi File & Struktur Vault
- Identifikasi jenis dokumen riset yang diproses (misal: *Literature Note*, *Synthesis Note*, *Research Gap Analysis*, atau *Full Workflow Export*).
- Tentukan hierarki folder Obsidian standar jika pengguna belum menentukannya, contoh:
  - `Vault/Literature/` (untuk catatan paper individu)
  - `Vault/Gaps & Hypotheses/` (untuk celah riset dan hipotesis)
  - `Vault/Synthesis/` (untuk sintesis dan matriks komparasi)
  - `Vault/Manuscript/` (untuk draf naskah utama)

### 2. Formulasi YAML Frontmatter Terstruktur
- Buat entri YAML Frontmatter di bagian teratas setiap file Markdown:
  ```yaml
  ---
  title: "Judul Catatan / Paper"
  aliases: ["Alias 1", "Shorthand"]
  tags:
    - research/literature
    - status/processed
    - quartile/q1
  authors: ["Author 1", "Author 2"]
  year: 2026
  doi: "10.xxxx/xxxxx"
  quartile: "Q1"
  sinta_rank: "S1"
  created: 2026-07-15
  ---
  ```

### 3. Konversi Tautan Teks ke Bidirectional WikiLinks
- Ubah rujukan teks biasa menjadi **WikiLinks 2 Arah** Obsidian:
  - Rujukan paper: `[Smith et al., 2025]` $\rightarrow$ `[[Literature Note - Smith 2025]]`
  - Rujukan celah riset: `Research Gap 1` $\rightarrow$ `[[Gap - Low Resource Paraphrasing]]`
  - Rujukan metode: `Transformer Model` $\rightarrow$ `[[Method - Transformer Architecture]]`

### 4. Penyusunan Dataview Queries & Diagram Visual
- Sertakan blok kode Dataview siap pakai pada catatan indeks/ringkasan:
  ```dataview
  TABLE authors, year, quartile, doi
  FROM "Literature"
  WHERE quartile = "Q1"
  SORT year DESC
  ```
- Pastikan seluruh diagram kerangka konseptual dikodekan menggunakan syntax Mermaid yang didukung Obsidian secara native.

### 5. Audit Keamanan Kredensial & Validasi File Output
- Pastikan tidak ada token API, kredensial private, atau path lokal sensitif di luar workspace yang terekspos dalam Frontmatter atau konten catatan.
- Sajikan dokumen Markdown hasil ekspor yang siap di-copypaste atau disimpan langsung ke Obsidian Vault pengguna.

## Common Mistakes & Aturan Kritis
- **Sintaks WikiLinks Rusak**: Menggunakan spasi ekstra atau karakter ilegal pada nama tautan WikiLink (misal `[[ Literature Note ]]` atau `[[File/Path:Invalid]]`).
- **YAML Frontmatter Tidak Valid**: Lupa menutup blok YAML dengan `---` atau menggunakan sintaks indentasi YAML yang melanggar standar spec.
- **Kebocoran Path Sensitif**: Menuliskan absolute path lokal sistem yang mengandung credential atau nama pengguna lokal secara publik.
- **Format Markdown Proprietary**: Menggunakan tag HTML kompleks yang tidak didukung atau merusak rendering markdown Obsidian native.
