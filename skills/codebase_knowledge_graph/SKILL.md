---
name: codebase-knowledge-graph
description: >-
  Bertugas memetakan arsitektur repositori/software proyek ke dalam Knowledge Graph terstruktur menggunakan Graphify (on-device Tree-sitter parsing & 10 MCP Tools) untuk query RAG presisi berbasis relasi, isolasi multi-proyek, dan ekspor Obsidian/Word terstandar.
---

# Codebase Knowledge Graph (Graphify Integration)

## Overview
Skill ini dirancang untuk memandu Research Agent dan Development Agent dalam menganalisis, memetakan, dan melacak arsitektur kode sumber (*source code*), skema basis data (SQL/PostgreSQL), infrastruktur (Terraform), serta dokumen pendukung pada proyek target ke dalam **Knowledge Graph terstruktur**.

Dengan mengintegrasikan engine **Graphify** (Apache 2.0, *on-device Tree-sitter parsing* 36+ bahasa), skill ini menggantikan pencarian *fuzzy vector RAG* tradisional dengan **path-based structural graph traversal**. Setiap relasi (*edge*) dilengkapi dengan tingkat kepastian (*confidence tag*: `EXTRACTED`, `INFERRED`, `AMBIGUOUS`) dan sitasi presisi hingga nomor baris (`file:line`).

## Dependencies
- `extract-methodology`
- `obsidian-vault-exporter`
- `journal-template-formatter`

## Quick Start
Contoh penggunaan:
> *"Petakan arsitektur repositori proyek ini ke dalam Knowledge Graph menggunakan Graphify, temukan modul sentral (god nodes), dan ekspor laporan arsitekturnya ke struktur Obsidian Vault serta format Word DOCX terstandar."*

---

## Workflow & Guidelines

### 1. Deteksi Target Proyek & Multi-Project Isolation
Untuk mendukung eksekusi multi-proyek secara bersamaan (*concurrent execution*) tanpa saling mencemari graph:
* **Proyek Lokal Saat Ini:** Eksekusi scan dilakukan di direktori akar (*root*) proyek target. Output otomatis disimpan di folder terisolasi `<Target_Project_Root>/graphify-out/`.
* **Proyek Eksternal / Multi-Project:** Jika menganalisis repositori luar (misalnya `/path/to/project-b`), selalu teruskan parameter `target_dir` sehingga graph proyek pendukung tidak mencemari ruang kerja repositori utama.

### 2. Instalasi & Registrasi Engine Graphify
Sebelum melakukan pemetaan, pastikan CLI `graphify` sudah terpasang dan terdaftar pada AI Assistant:
```bash
# Instalasi via UV (rekomendasi) atau Pipx
uv tool install graphifyy

# Registrasi skill ke AI Coding Assistants (Claude Code, Cursor, Copilot, Aider, dll)
graphify install
```

### 3. Pemetaan Repositori (Building the Graph)
Jalankan perintah pemetaan di dalam lingkungan assistant atau terminal:
```bash
# Pemetaan penuh repositori
/graphify .

# Pemetaan inkremental (hanya perubahan berkas)
/graphify . --update

# Pemetaan mendalam (multi-pass architecture analysis)
/graphify . --mode deep
```
**Output yang Dihasilkan (`graphify-out/`):**
* `graphify-out/graph.html`: Visualisasi grafik interaktif 2D/3D.
* `graphify-out/GRAPH_REPORT.md`: Laporan arsitektur dan keterhubungan modul.
* `graphify-out/graph.json`: Berkas Graph JSON *machine-readable* untuk query MCP.

### 4. Query & Traversal Berbasis MCP Server / CLI
Agen dapat memanfaatkan **10 MCP Tools** (jika `graphify.serve` aktif) atau perintah CLI untuk menggali struktur kode secara presisi:

| MCP Tool | CLI Equivalent | Fungsi Utama |
| :--- | :--- | :--- |
| `query_graph` | `graphify query "<prompt>"` | Query hubungan antar modul/fungsi berbasis teks alami. |
| `shortest_path` | `graphify path "<A>" "<B>"` | Menemukan jalur terpendek penghubung dua kelas/modul. |
| `get_node` | `graphify explain "<Node>"` | Mengambil detail spesifik, fungsi pemanggil, dan pemanggilan modul. |
| `god_nodes` | `graphify stats` | Mengidentifikasi modul/kelas sentral (*core bottlenecks/central hubs*). |
| `get_neighbors` | - | Melihat seluruh entitas yang terhubung langsung dengan suatu node. |
| `get_community` | - | Mengelompokkan komponen ke dalam *cluster/subsystem* arsitektur. |
| `graph_stats` | - | Mengambil statistik ringkasan total node, edge, dan bahasa. |
| `list_prs`, `get_pr_impact`, `triage_prs` | - | Menganalisis dampak perubahan Pull Request terhadap komponen lain di graph. |

---

### 5. Multi-Project Obsidian Vault Export Strategy
Saat mengekspor luaran Knowledge Graph ke **Obsidian Vault** (*Second Brain*), terapkan aturan isolasi ketat agar tidak bercampur antar-proyek:

1. **Subfolder Terisolasi:** Tempatkan file ekspor di subfolder terpisah per nama proyek:
   `Obsidian_Vaults/<project_name>/Graphify/`
2. **YAML Frontmatter Metadata Scoping:**
   ```yaml
   ---
   project: "<project_name>"
   type: "code-knowledge-graph"
   source: "Graphify Engine"
   created: 2026-07-31
   tags:
     - project/<project_name>
     - graphify/code-graph
   ---
   ```
3. **Scoped Dataview Query:**
   ```dataview
   TABLE type, file.mtime
   FROM "Projects/<project_name>/Graphify"
   WHERE project = "<project_name>"
   ```
4. **WikiLinks Namespacing:** Berikan prefix nama proyek pada tautan 2 arah (`[[ProjectName/ModuleName]]`) untuk mencegah tabrakan nama note di *Obsidian Graph View*.

---

### 6. Standar Pemformatan Dokumen DOCX (Word Built-in Styles)
Apabila laporan arsitektur (`GRAPH_REPORT.md`) atau rangkuman hasil ekstraksi diekspor ke dalam format MS Word (`.docx`), agen **WAJIB** menerapkan standar gaya bawaan Word (*Word Built-in Styles*) berikut:

1. **Gaya Paragraf `Normal` (Default Body Text):**
   * **Alignment:** **Rata Kiri-Kanan (Justified / `w:jc w:val="both"`)**.
   * **Line Spacing:** **1.15 - 1.5**.
   * **Paragraph Spacing:** **Space After 6pt** (mencegah *double enter* manual).
   * **Font:** Times New Roman / Calibri / Inter (11pt / 12pt).
2. **Gaya `Heading 1` s/d `Heading 4` (Native Word Hierarchy):**
   * Terhubung langsung dengan *Word Navigation Pane* & *Table of Contents (TOC)*.
   * `Heading 1`: 16pt Bold, Space Before 12pt, After 6pt.
   * `Heading 2`: 14pt Bold, Space Before 10pt, After 4pt.
   * `Heading 3`: 12pt Bold/Italic, Space Before 6pt, After 2pt.
   * Fitur Kritis: `keep_with_next = True` (mencegah judul terpisah dari paragraf pertama di bawahnya).
3. **List & Table Styles:**
   * `List Paragraph`: Indentasi bullet/numbering teratur.
   * `Caption`: Rata tengah (*center-aligned*), miring (*italic*), ukuran 9.5-10pt.

---

## Few-Shot Guidance

### ❌ [SALAH] Query Mengambang & Dokumen Tidak Terstandar
> **Agent Answer:** "Modul auth sepertinya terhubung dengan database via session."  
> **DOCX Export:** Paragraf rata kiri (*left-aligned*), tanpa pemformatan gaya `Normal`, menggunakan enter manual 2x antar paragraf, dan heading berbentuk teks biasa yang di-bold tanpa hirarki *Word Navigation Pane*.

### ✅ [BENAR] Graphify Grounding & DOCX Terstandar
> **Agent Answer:**  
> `AuthService → SessionStore → DatabasePool [EXTRACTED]`  
> `Location: src/auth/service.py:42 → src/db/pool.py:17`  
> **DOCX Export:** Seluruh paragraf teks biasa terformat dengan gaya `Normal` (Justified rata kiri-kanan, spasi 1.15, space after 6pt), serta judul bab terstruktur dengan hierarki `Heading 1-3` (*keep_with_next = True*).
