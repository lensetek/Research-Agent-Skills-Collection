# Research Agent Skills Collection

*Read this in other languages: [English](#english), [Bahasa Indonesia](#bahasa-indonesia).*

---

### 🔥 What's New / Yang Baru (June 2026)
* **🇮🇩 Upgrade Skill Eksplorasi Celah (Gap)**: `discover-phenomenon-and-gap` kini menggunakan strategi *Survey of Surveys* dan *Batch Processing* untuk mensintesis ide dari ratusan paper tanpa token limit, serta dilengkapi indikator *Skala Kesulitan*.
* **🇬🇧 Gap Exploration Skill Upgrade**: `discover-phenomenon-and-gap` now utilizes *Survey of Surveys* and *Batch Processing* strategies to synthesize ideas from hundreds of papers without token limits, complete with a *Difficulty Scale* indicator.
* **🇮🇩 Keamanan Anti-Halusinasi Global**: Diterapkan kebijakan *Zero-Tolerance* terhadap data/paper fiktif di seluruh agen (Orkestrator, Akuisisi Data, Ekstraksi Metodologi, dan Matriks) untuk menjamin integritas riset.
* **🇬🇧 Global Anti-Hallucination Security**: Enforced a Zero-Tolerance policy against fake data/papers across all agents (Orchestrator, Data Acquisition, Extract Methodology, and Matrix Builder) to ensure research integrity.
* **🇮🇩 Upgrade Skill SLR (PRISMA Funnel)**: `literature-review-generator` kini mengintegrasikan alur kerja PRISMA 4-tahap dengan filter otomatis Python dan checkpoint CSV untuk menangani ribuan paper.
* **🇬🇧 SLR Skill Upgrade (PRISMA Funnel)**: `literature-review-generator` now integrates a 4-step PRISMA workflow with automated Python filtering and CSV checkpoints to handle thousands of papers.
* **🇮🇩 1 Skill Validator Baru**: Ditambahkan `model-evaluator-validator` (Fase 2) untuk menguji signifikansi statistik (T-Test, Diebold-Mariano) dari hasil prediksi model. Total skill kini menjadi 22.
* **🇬🇧 1 New Validator Skill**: Added `model-evaluator-validator` (Phase 2) to test the statistical significance of model predictions. Total skills are now 22.
* **🇮🇩 1 Skill Baru (Digital Twin)**: Ditambahkan `synthetic-data-generator` (Fase 2) untuk meng-generate dataset sintetis kuantitatif/kualitatif dengan mensimulasikan persona responden.
* **🇬🇧 1 New Skill (Digital Twin)**: Added `synthetic-data-generator` (Phase 2) to generate quantitative/qualitative synthetic datasets by simulating respondent personas.
* **🇮🇩 2 Skill Data Baru**: Ditambahkan `data-acquisition-specialist` untuk akuisisi/scraping data, dan `data-scientist-analyst` untuk olah data statistik/ML pada Fase 2. `research-orchestrator` telah diperbarui untuk mendukung alur kerja 22 skill.
* **🇬🇧 2 New Data Skills**: Added `data-acquisition-specialist` for data acquisition/scraping, and `data-scientist-analyst` for statistical/ML data processing in Phase 2. `research-orchestrator` has been updated to support the 22-skill workflow.
* **🇮🇩 Fitur Personalisasi Implisit Baru**: Ditambahkan Fase 5 ke dalam `research-orchestrator`. Agen sekarang secara otomatis membaca preferensi Anda dari `user_profile.json` di awal sesi dan merekam umpan balik Anda secara implisit ke dalam file tersebut di akhir sesi agar riset berikutnya berjalan lebih cerdas.
* **🇬🇧 New Implicit Personalization Feature**: Added Phase 5 to the `research-orchestrator`. The agent now automatically loads your preferences from `user_profile.json` at the start of a session and implicitly records your feedback back into the file at the end of the session to make subsequent runs smarter.

---

## Bahasa Indonesia

Repositori ini adalah kumpulan **Skills** khusus untuk **Research Agent** (Asisten Agen Peneliti). Kumpulan skill ini dipasang langsung ke dalam sistem plugin `science` untuk membekali agen AI dengan prosedur metodologis ilmiah yang kokoh dalam mencari, menganalisis, mengekstrak, dan mengevaluasi literatur akademis serta paten teknologi secara valid tanpa halusinasi.

### Kumpulan Skill yang Tersedia (22 Skills)

#### 🚀 Orkestrator Utama (Starter Skill)
*   **[research-orchestrator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_orchestrator/SKILL.md)**: Pintu masuk utama untuk menjalankan alur kerja riset 5 fase otomatis penuh (termasuk personalisasi implisit) secara sekuensial.

#### 📁 Fase 1 — Discovery & Framing (Masalah)
1.  **[discover-phenomenon-and-gap](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/discover_phenomenon_and_gap/SKILL.md)**: Eksplorasi tren fenomena baru, anomali, dan pemetaan celah ilmiah (*research gap*) formal.
2.  **[research-question-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_question_builder/SKILL.md)**: Mengubah celah riset menjadi Pertanyaan Riset (RQ), tujuan penelitian, kontribusi, dan batasan ruang lingkup (*scope limitation*).
3.  **[hypothesis-or-proposition-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/hypothesis_or_proposition_builder/SKILL.md)**: Menyusun pernyataan hipotesis/proposisi logis disertai diagram Mermaid kerangka konseptual.

#### 📁 Fase 2 — Research Methodology & Computational Experiments (Perencanaan & Eksperimen)
4.  **[research-design-planner](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_design_planner/SKILL.md)**: Merancang desain metode (kuantitatif, kualitatif, mixed-method, komputasional AI/ML) beserta skenario validasi, pengujian robustness, dan studi ablasi.
5.  **[synthetic-data-generator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/synthetic_data_generator/SKILL.md)**: Bertindak sebagai Digital Twin / Persona Simulator untuk meng-generate dataset sintetis (kuantitatif & kualitatif) dalam skala besar menggunakan LLM.
6.  **[data-acquisition-specialist](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/data_acquisition_specialist/SKILL.md)**: Mencari, mengumpulkan, mengunduh, dan melakukan web scraping data (baik statis maupun dinamis) dari berbagai sumber internet/API tanpa batasan guna menyusun dataset penelitian yang terstruktur.
7.  **[data-scientist-analyst](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/data_scientist_analyst/SKILL.md)**: Memproses, menganalisis, menguji statistik (regresi, PLS), melatih model Machine Learning, dan membuat visualisasi data ilmiah secara terstruktur.
8.  **[model-evaluator-validator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/model_evaluator_validator/SKILL.md)**: Mengevaluasi dan memvalidasi signifikansi statistik (T-Test, ANOVA, Diebold-Mariano) dari hasil prediksi model guna memastikan ketangguhan riset.

#### 📁 Fase 3 — Literature Intelligence (Kajian & Validasi)
9.  **[literature-review-generator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/literature_review_generator/SKILL.md)**: Penyusunan draf tinjauan pustaka bertema dengan mode khusus (Narrative, SLR, Thematic, Chronological, Critical) dan Peta Argumen.
10. **[extract-methodology](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/extract_methodology/SKILL.md)**: Membedah paper untuk ekstraksi 10 komponen teknis wajib (tujuan, parameter, dataset, dll.).
11. **[source-quality-appraiser](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/source_quality_appraiser/SKILL.md)**: Menilai kuartil jurnal (Q1-Q4), peringkat konferensi (CORE), bias metodologis, dan status kelayakan rujukan.
12. **[citation-and-reference-validator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/citation_and_reference_validator/SKILL.md)**: Audit keaslian rujukan (DOI) dan memvalidasi dukungan kontekstual kalimat rujukan (mencegah salah sitasi).
13. **[paper-matrix-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/paper_matrix_builder/SKILL.md)**: Mengotomatiskan pembuatan tabel ringkasan komparasi State-of-the-Art (SotA) dan peta bukti (*evidence map*).

#### 📁 Fase 4 — Synthesis, Novelty & Publication (Sintesis & Publikasi)
14. **[synthesize-research](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/synthesize_research/SKILL.md)**: Analisis komparasi temuan kritis, memetakan konsensus & kontradiksi, serta memisahkan opini dari bukti rujukan.
15. **[patent-and-literature-matcher](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/patent_and_literature_matcher/SKILL.md)**: Mendeteksi potensi *prior art* dengan mencocokkan komponen klaim invensi terhadap literatur ilmiah.
16. **[journal-recommendation-finder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/journal_recommendation_finder/SKILL.md)**: Mencari jurnal target terbaik berdasarkan kuartil, relevansi scope, biaya APC, dan turnaround time (bebas jurnal predator).
17. **[academic-peer-reviewer](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/academic_peer_reviewer/SKILL.md)**: Simulasi peer review independen (Accept/Revision/Reject) dengan daftar masalah mayor/minor.
18. **[reviewer-response-and-revision](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/reviewer_response_and_revision/SKILL.md)**: Memformulasikan draf jawaban diplomatis *Response to Reviewers* dan merencanakan revisi naskah secara konsisten.
19. **[academic-paraphraser](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/academic_paraphraser/SKILL.md)**: Memparafrase dan menghumanisasi teks akademik secara struktural untuk menghindari plagiasi dan menjaga makna asli.
20. **[advanced-similarity-reducer](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/advanced_similarity_reducer/SKILL.md)**: Skill tingkat lanjut (ultra-advance) untuk merombak total struktur paragraf secara konseptual guna menurunkan skor similarity (Turnitin) secara ekstrem tanpa mengubah makna.

#### 📁 Fase 5 — Personalization & Memori (Personalisasi)
21. **[user_profile.json](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/user_profile.json)** (Root): Berkas profil penelitian pengguna yang diperbarui secara implisit oleh orkestrator di akhir sesi untuk menyimpan gaya penulisan, target jurnal, dan preferensi riset.

#### 🔧 Utilitas (Maintenance & Update)
22. **[agent-update-checker](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/agent_update_checker/SKILL.md)**: Bertugas mengecek pembaruan agen secara berkala dari repositori dan menawarkan instalasi pembaruan melalui prompt URL.

---

## English

This repository is a collection of custom **Skills** for **Research Agents**. These skills are directly installed into the `science` plugin system to equip AI agents with solid scientific methodology procedures to search, analyze, extract, and evaluate academic literature and technology patents factually without hallucination.

### Available Skills (22 Skills)

#### 🚀 Main Orchestrator (Starter Skill)
*   **[research-orchestrator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_orchestrator/SKILL.md)**: Main entry point to run the full 5-phase research workflow sequentially and automatically (including implicit personalization).

#### 📁 Phase 1 — Discovery & Framing (Problem Framing)
1.  **[discover-phenomenon-and-gap](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/discover_phenomenon_and_gap/SKILL.md)**: Explores new phenomenon trends, anomalies, and maps formal academic research gaps.
2.  **[research-question-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_question_builder/SKILL.md)**: Translates gaps into Research Questions (RQs), research objectives, theoretical/methodological/practical contributions, and scope limitations.
3.  **[hypothesis-or-proposition-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/hypothesis_or_proposition_builder/SKILL.md)**: Formulates directional hypotheses or qualitative propositions with conceptual framework diagrams (Mermaid format).

#### 📁 Phase 2 — Research Methodology & Computational Experiments (Planning & Experiments)
4.  **[research-design-planner](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/research_design_planner/SKILL.md)**: Designs methodologies (quantitative, qualitative, mixed-methods, computational AI/ML experiments) with validations, robustness checks, and ablation plans.
5.  **[synthetic-data-generator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/synthetic_data_generator/SKILL.md)**: Acts as a Digital Twin / Persona Simulator to generate synthetic datasets (quantitative & qualitative) on a large scale using LLMs.
6.  **[data-acquisition-specialist](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/data_acquisition_specialist/SKILL.md)**: Searches, collects, downloads, and performs web scraping (static or dynamic) from various internet sources/APIs without limits to compile structured research datasets.
7.  **[data-scientist-analyst](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/data_scientist_analyst/SKILL.md)**: Processes, analyzes, performs statistical testing (regression, PLS), trains Machine Learning models, and creates structured scientific data visualizations.
8.  **[model-evaluator-validator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/model_evaluator_validator/SKILL.md)**: Evaluates and validates the statistical significance (T-Test, ANOVA, Diebold-Mariano) of model predictions to ensure research robustness.

#### 📁 Phase 3 — Literature Intelligence (Review & Audit)
9.  **[literature-review-generator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/literature_review_generator/SKILL.md)**: Generates structured, themed literature reviews using specific modes (Narrative, SLR, Thematic, Chronological, Critical) with Argument Maps.
10. **[extract-methodology](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/extract_methodology/SKILL.md)**: Dissects papers to extract 10 mandatory technical components (objectives, parameters, datasets, metrics, etc.).
11. **[source-quality-appraiser](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/source_quality_appraiser/SKILL.md)**: Appraises journal quartiles (Q1-Q4), conference rankings (CORE), methodological flaws, bias risks, and overall reference eligibility.
12. **[citation-and-reference-validator](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/citation_and_reference_validator/SKILL.md)**: Audits citation metadata (DOIs) and validates contextual citation support (preventing misattribution/fake citations).
13. **[paper-matrix-builder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/paper_matrix_builder/SKILL.md)**: Automates the creation of standardized State-of-the-Art (SotA) matrices and evidence maps.

#### 📁 Phase 4 — Synthesis, Novelty & Publication (Synthesis & Publishing)
14. **[synthesize-research](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/synthesize_research/SKILL.md)**: Compares critical findings, maps consensuses and debates, and separates objective evidence from agent interpretation.
15. **[patent-and-literature-matcher](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/patent_and_literature_matcher/SKILL.md)**: Discovers potential prior art by mapping patent/invention claims against scientific publications.
16. **[journal-recommendation-finder](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/journal_recommendation_finder/SKILL.md)**: Discovers ideal target journals by quartile, scope alignment, APC costs, and turnaround times, avoiding predatory venues.
17. **[academic-peer-reviewer](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/academic_peer_reviewer/SKILL.md)**: Simulates peer reviews (Accept/Revision/Reject) with categorized major and minor concerns.
18. **[reviewer-response-and-revision](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/reviewer_response_and_revision/SKILL.md)**: Drafts formal Responses to Reviewers and plans manuscript modifications consistently.
19. **[academic-paraphraser](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/academic_paraphraser/SKILL.md)**: Paraphrases and humanizes academic texts using advanced structural rewriting to avoid plagiarism while preserving original meaning.
20. **[advanced-similarity-reducer](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/advanced_similarity_reducer/SKILL.md)**: Ultra-advanced skill to completely restructure paragraphs conceptually, drastically reducing similarity scores (Turnitin) without losing academic weight or original meaning.

#### 📁 Phase 5 — Personalization & Memory (Personalization)
21. **[user_profile.json](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/user_profile.json)** (Root): User research profile file updated implicitly by the orchestrator at the end of a session to store writing styles, target journals, and research preferences.

#### 🔧 Utility (Maintenance & Update)
22. **[agent-update-checker](file:///C:/Users/ACER/Documents/antigravity/Research-Agent/skills/agent_update_checker/SKILL.md)**: Responsible for periodically checking for agent updates from the repository and offering update installations via a URL prompt.

---

## Dependensi Sistem Pencarian / Search System Dependencies

Seluruh skill ini memanfaatkan modul pencarian literatur bawaan sistem / All these skills utilize the system's built-in literature search modules:
*   **arXiv API** (`literature-search-arxiv`)
*   **OpenAlex API** (`literature-search-openalex`)
*   **bioRxiv/medRxiv API** (`literature-search-biorxiv`)
*   **PubMed/Entrez API** (`pubmed-database`)
*   **Europe PMC API** (`literature-search-europepmc`)

---

## Instalasi via Prompt / Installation via Prompt

### 🇮🇩 Bahasa Indonesia
Anda dapat memasang seluruh skill ini secara langsung menggunakan perintah/prompt kepada agen Anda:

1. **Prompt Instalasi**:
   Kirimkan perintah (*prompt*) berikut ke agen Anda untuk mengunduh dan memasang repositori:
   ```text
   Tolong download dan install agent skill dari url https://github.com/lensetek/Research-Agent-Skills-Collection
   ```

2. **Konfirmasi Pemasangan**:
   Kirimkan perintah (*prompt*) berikut untuk memverifikasi jumlah skill yang terpasang di proyek ini:
   ```text
   Konfirmasi berapa agent skill yang ada di project ini?
   ```

---

### 🇬🇧 English
You can install all these skills directly using prompt commands to your agent:

1. **Installation Prompt**:
   Send the following prompt to your agent to download and install the repository:
   ```text
   Please download and install the agent skills from the URL https://github.com/lensetek/Research-Agent-Skills-Collection
   ```

2. **Installation Confirmation**:
   Send the following prompt to verify the number of installed skills in this project:
   ```text
   Confirm how many agent skills are in this project?
   ```

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
