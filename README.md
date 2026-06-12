# Research Agent Skills Collection

*Read this in other languages: [English](#english), [Bahasa Indonesia](#bahasa-indonesia).*

---

### 🔥 What's New / Yang Baru (June 2026)
* **🇮🇩 Fitur Personalisasi Implisit Baru**: Ditambahkan Fase 5 ke dalam `research-orchestrator`. Agen sekarang secara otomatis membaca preferensi Anda dari `user_profile.json` di awal sesi dan merekam umpan balik Anda secara implisit ke dalam file tersebut di akhir sesi agar riset berikutnya berjalan lebih cerdas.
* **🇬🇧 New Implicit Personalization Feature**: Added Phase 5 to the `research-orchestrator`. The agent now automatically loads your preferences from `user_profile.json` at the start of a session and implicitly records your feedback back into the file at the end of the session to make subsequent runs smarter.

---

## Bahasa Indonesia

Repositori ini adalah kumpulan **Skills** khusus untuk **Research Agent** (Asisten Agen Peneliti). Kumpulan skill ini dipasang langsung ke dalam sistem plugin `science` untuk membekali agen AI dengan prosedur metodologis ilmiah yang kokoh dalam mencari, menganalisis, mengekstrak, dan mengevaluasi literatur akademis serta paten teknologi secara valid tanpa halusinasi.

### Kumpulan Skill yang Tersedia (16 Skills)

#### 🚀 Orkestrator Utama (Starter Skill)
*   **[research-orchestrator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_orchestrator/SKILL.md)**: Pintu masuk utama untuk menjalankan alur kerja riset 5 fase otomatis penuh (termasuk personalisasi implisit) secara sekuensial.

#### 📁 Fase 1 — Discovery & Framing (Masalah)
1.  **[discover-phenomenon-and-gap](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/discover_phenomenon_and_gap/SKILL.md)**: Eksplorasi tren fenomena baru, anomali, dan pemetaan celah ilmiah (*research gap*) formal.
2.  **[research-question-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_question_builder/SKILL.md)**: Mengubah celah riset menjadi Pertanyaan Riset (RQ), tujuan penelitian, kontribusi, dan batasan ruang lingkup (*scope limitation*).
3.  **[hypothesis-or-proposition-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/hypothesis_or_proposition_builder/SKILL.md)**: Menyusun pernyataan hipotesis/proposisi logis disertai diagram Mermaid kerangka konseptual.

#### 📁 Fase 2 — Research Methodology (Perencanaan)
4.  **[research-design-planner](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_design_planner/SKILL.md)**: Merancang desain metode (kuantitatif, kualitatif, mixed-method, komputasional AI/ML) beserta skenario validasi, pengujian robustness, dan studi ablasi.

#### 📁 Fase 3 — Literature Intelligence (Kajian & Validasi)
5.  **[literature-review-generator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/literature_review_generator/SKILL.md)**: Penyusunan draf tinjauan pustaka bertema dengan mode khusus (Narrative, SLR, Thematic, Chronological, Critical) dan Peta Argumen.
6.  **[extract-methodology](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/extract_methodology/SKILL.md)**: Membedah paper untuk ekstraksi 10 komponen teknis wajib (tujuan, parameter, dataset, dll.).
7.  **[source-quality-appraiser](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/source_quality_appraiser/SKILL.md)**: Menilai kuartil jurnal (Q1-Q4), peringkat konferensi (CORE), bias metodologis, dan status kelayakan rujukan.
8.  **[citation-and-reference-validator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/citation_and_reference_validator/SKILL.md)**: Audit keaslian rujukan (DOI) dan memvalidasi dukungan kontekstual kalimat rujukan (mencegah salah sitasi).
9.  **[paper-matrix-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/paper_matrix_builder/SKILL.md)**: Mengotomatiskan pembuatan tabel ringkasan komparasi State-of-the-Art (SotA) dan peta bukti (*evidence map*).

#### 📁 Fase 4 — Synthesis, Novelty & Publication (Sintesis & Publikasi)
10. **[synthesize-research](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/synthesize_research/SKILL.md)**: Analisis komparasi temuan kritis, memetakan konsensus & kontradiksi, serta memisahkan opini dari bukti rujukan.
11. **[patent-and-literature-matcher](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/patent_and_literature_matcher/SKILL.md)**: Mendeteksi potensi *prior art* dengan mencocokkan komponen klaim invensi terhadap literatur ilmiah.
12. **[journal-recommendation-finder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/journal_recommendation_finder/SKILL.md)**: Mencari jurnal target terbaik berdasarkan kuartil, relevansi scope, biaya APC, dan turnaround time (bebas jurnal predator).
13. **[academic-peer-reviewer](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/academic_peer_reviewer/SKILL.md)**: Simulasi peer review independen (Accept/Revision/Reject) dengan daftar masalah mayor/minor.
14. **[reviewer-response-and-revision](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/reviewer_response_and_revision/SKILL.md)**: Memformulasikan draf jawaban diplomatis *Response to Reviewers* dan merencanakan revisi naskah secara konsisten.
15. **[academic-paraphraser](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/academic_paraphraser/SKILL.md)**: Memparafrase dan menghumanisasi teks akademik secara struktural untuk menghindari plagiasi dan menjaga makna asli.

#### 📁 Fase 5 — Personalization & Memori (Personalisasi)
16. **[user_profile.json](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/user_profile.json)** (Root): Berkas profil penelitian pengguna yang diperbarui secara implisit oleh orkestrator di akhir sesi untuk menyimpan gaya penulisan, target jurnal, dan preferensi riset.

---

## English

This repository is a collection of custom **Skills** for **Research Agents**. These skills are directly installed into the `science` plugin system to equip AI agents with solid scientific methodology procedures to search, analyze, extract, and evaluate academic literature and technology patents factually without hallucination.

### Available Skills (16 Skills)

#### 🚀 Main Orchestrator (Starter Skill)
*   **[research-orchestrator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_orchestrator/SKILL.md)**: Main entry point to run the full 5-phase research workflow sequentially and automatically (including implicit personalization).

#### 📁 Phase 1 — Discovery & Framing (Problem Framing)
1.  **[discover-phenomenon-and-gap](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/discover_phenomenon_and_gap/SKILL.md)**: Explores new phenomenon trends, anomalies, and maps formal academic research gaps.
2.  **[research-question-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_question_builder/SKILL.md)**: Translates gaps into Research Questions (RQs), research objectives, theoretical/methodological/practical contributions, and scope limitations.
3.  **[hypothesis-or-proposition-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/hypothesis_or_proposition_builder/SKILL.md)**: Formulates directional hypotheses or qualitative propositions with conceptual framework diagrams (Mermaid format).

#### 📁 Phase 2 — Research Methodology (Planning)
4.  **[research-design-planner](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_design_planner/SKILL.md)**: Designs methodologies (quantitative, qualitative, mixed-methods, computational AI/ML experiments) with validations, robustness checks, and ablation plans.

#### 📁 Phase 3 — Literature Intelligence (Review & Audit)
5.  **[literature-review-generator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/literature_review_generator/SKILL.md)**: Generates structured, themed literature reviews using specific modes (Narrative, SLR, Thematic, Chronological, Critical) with Argument Maps.
6.  **[extract-methodology](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/extract_methodology/SKILL.md)**: Dissects papers to extract 10 mandatory technical components (objectives, parameters, datasets, metrics, etc.).
7.  **[source-quality-appraiser](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/source_quality_appraiser/SKILL.md)**: Appraises journal quartiles (Q1-Q4), conference rankings (CORE), methodological flaws, bias risks, and overall reference eligibility.
8.  **[citation-and-reference-validator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/citation_and_reference_validator/SKILL.md)**: Audits citation metadata (DOIs) and validates contextual citation support (preventing misattribution/fake citations).
9.  **[paper-matrix-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/paper_matrix_builder/SKILL.md)**: Automates the creation of standardized State-of-the-Art (SotA) matrices and evidence maps.

#### 📁 Phase 4 — Synthesis, Novelty & Publication (Synthesis & Publishing)
10. **[synthesize-research](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/synthesize_research/SKILL.md)**: Compares critical findings, maps consensuses and debates, and separates objective evidence from agent interpretation.
11. **[patent-and-literature-matcher](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/patent_and_literature_matcher/SKILL.md)**: Discovers potential prior art by mapping patent/invention claims against scientific publications.
12. **[journal-recommendation-finder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/journal_recommendation_finder/SKILL.md)**: Discovers ideal target journals by quartile, scope alignment, APC costs, and turnaround times, avoiding predatory venues.
13. **[academic-peer-reviewer](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/academic_peer_reviewer/SKILL.md)**: Simulates peer reviews (Accept/Revision/Reject) with categorized major and minor concerns.
14. **[reviewer-response-and-revision](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/reviewer_response_and_revision/SKILL.md)**: Drafts formal Responses to Reviewers and plans manuscript modifications consistently.
15. **[academic-paraphraser](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/academic_paraphraser/SKILL.md)**: Paraphrases and humanizes academic texts using advanced structural rewriting to avoid plagiarism while preserving original meaning.

#### 📁 Phase 5 — Personalization & Memory (Personalization)
16. **[user_profile.json](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/user_profile.json)** (Root): User research profile file updated implicitly by the orchestrator at the end of a session to store writing styles, target journals, and research preferences.

---

## Dependensi Sistem Pencarian / Search System Dependencies

Seluruh skill ini memanfaatkan modul pencarian literatur bawaan sistem / All these skills utilize the system's built-in literature search modules:
*   **arXiv API** (`literature-search-arxiv`)
*   **OpenAlex API** (`literature-search-openalex`)
*   **bioRxiv/medRxiv API** (`literature-search-biorxiv`)
*   **PubMed/Entrez API** (`pubmed-database`)
*   **Europe PMC API** (`literature-search-europepmc`)

---

## Instalasi via Git & Prompt / Installation via Git & Prompt

### 🇮🇩 Bahasa Indonesia
Anda dapat memasang seluruh 16 skill ini dengan melakukan kloning repositori dan menggunakan *prompt* kepada agen untuk memuatnya.

1.  **Kloning Repositori**:
    Jalankan perintah berikut di terminal Anda:
    ```bash
    git clone https://github.com/lensetek/Research-Agent-Skills-Collection.git
    ```
    *(Atau gunakan `git pull` jika Anda sudah pernah melakukan kloning sebelumnya).*

2.  **Gunakan Prompt**:
    Berikan instruksi (*prompt*) berikut kepada agen Anda:
    > *"Tolong baca folder skill dari repositori yang baru saja saya clone, lalu muat dan daftarkan seluruh skill tersebut ke dalam sistem Anda."*

---

### 🇬🇧 English
You can install all 16 skills by cloning the repository and using a prompt to instruct the agent to load them.

1.  **Clone the Repository**:
    Run the following command in your terminal:
    ```bash
    git clone https://github.com/lensetek/Research-Agent-Skills-Collection.git
    ```
    *(Or use `git pull` if you have previously cloned it).*

2.  **Use Prompt**:
    Give the following prompt to your agent:
    > *"Please read the skills folder from the newly cloned repository, then load and register all the skills into your system."*

---

## Cara Menggunakan Skill / How to Use the Skills

### 🚀 1. Alur Orkestrasi Otomatis (Automatic Orchestration Flow - RECOMMENDED)

#### 🇮🇩 Bahasa Indonesia
Untuk memulai seluruh alur penelitian otomatis dari satu pintu masuk, jalankan skill **`research-orchestrator`** dengan memberikan topik atau domain riset Anda.

> **ID**: *"Gunakan skill **research-orchestrator** untuk memulai riset otomatis penuh tentang efektivitas Graph Neural Networks dalam fraud detection transaksi keuangan."*

Setelah diaktifkan, agen akan menjalankan Fase 1 hingga Fase 5 secara otomatis dan memberikan keluaran akhir berupa **Integrated Research Dashboard** serta pembaruan profil personal (`user_profile.json`).

---

#### 🇬🇧 English
To start the entire automated research workflow from a single entry point, run the **`research-orchestrator`** skill by providing your research topic or domain.

> **EN**: *"Use the **research-orchestrator** skill to start a full automatic research flow on the effectiveness of Graph Neural Networks for financial transaction fraud detection."*

Once activated, the agent will run Phase 1 to Phase 5 automatically and provide the final output in the form of an **Integrated Research Dashboard** and personal profile updates (`user_profile.json`).

---

### 🛠️ 2. Menjalankan Skill Secara Terpisah (Individual Execution)
Anda juga dapat memicu setiap skill secara terpisah menggunakan perintah berbahasa alami:

> **ID**: *"Gunakan skill **academic-peer-reviewer** untuk meninjau draf paper ini secara kritis."*
>
> **EN**: *"Use the **academic-peer-reviewer** skill to critically review this manuscript draft."*

---

## Personalization & Memori Riset / Personalization & Research Memory

### 🇮🇩 Bahasa Indonesia
Sistem ini mendukung **Implicit Personalization** secara otomatis:
* **Membaca Profil**: Di awal eksekusi `research-orchestrator`, agen akan mencari dan memuat preferensi dari berkas `user_profile.json` di root direktori (jika ada).
* **Belajar secara Implisit**: Di akhir sesi, agen akan menganalisis percakapan/umpan balik Anda secara otomatis dan memperbarui berkas `user_profile.json` agar sesi berikutnya semakin pintar dan terpersonalisasi.

### 🇬🇧 English
This system automatically supports **Implicit Personalization**:
* **Load Profile**: At the start of `research-orchestrator` execution, the agent looks for and loads preferences from `user_profile.json` at the root directory (if present).
* **Implicit Learning**: At the end of the session, the agent analyzes your conversation/feedback and automatically updates `user_profile.json` to make subsequent sessions smarter and more personalized.
