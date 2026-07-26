#!/usr/bin/env python3
"""
Master HITL (Human-in-the-Loop) Research Evaluation Checklist Generator & Manager.
Creates and updates hitl_research_checklist.md across all research phases.
"""

import argparse
import datetime
import json
import os
import sys

PHASES = {
    "1": {
        "title": "💡 FASE 1: Eksplorasi Topik & Formulasi Masalah",
        "skills": "discover_phenomenon_and_gap, research_question_builder, hypothesis_or_proposition_builder",
        "items": [
            "**Phenomenon & Novelty**: Fenomena ilmiah/teknologi yang diidentifikasi memiliki kebaruan dan didukung publikasi literatur terbaru.",
            "**Research Gap**: Celah penelitian (gap) terdefinisi secara presisi dan belum diselesaikan oleh studi terdahulu.",
            "**Research Questions & Hypotheses**: Rumusan masalah dan hipotesis terstruktur dengan variabel/konstruk yang terukur."
        ]
    },
    "2": {
        "title": "📋 FASE 2: Desain Penelitian & Akuisisi Data",
        "skills": "research_design_planner, data_acquisition_specialist",
        "items": [
            "**Methodological Design**: Pendekatan metodologi (Kuantitatif / Kualitatif / Mixed-Method) selaras dengan pertanyaan penelitian.",
            "**Data Source Credibility**: Sumber data (web scraping / API / database) kredibel dan memenuhi etika pengumpulan data.",
            "**Data Privacy & PII Guardrail**: Dataset telah dipindai dan dipastikan bebas dari API Key, password, atau data pribadi sensitif."
        ]
    },
    "3": {
        "title": "💻 FASE 3: Komputasi Perangkat, Analisis Data & Model Training",
        "skills": "hardware_workload_estimator, data_scientist_analyst, model_evaluator_validator",
        "items": [
            "**Hardware Runtime Choice**: Menyetujui keputusan eksekusi komputasi (Lokal Mesin vs Google Colab GPU).",
            "**Statistical Assumptions**: Uji asumsi statistik (normalitas, homogenitas, linieritas, dll.) teruji dan terpenuhi.",
            "**ML Performance & Overfitting Check**: Metrik evaluasi (R2, F1-Score, RMSE, ROC-AUC) valid dan bebas dari data leakage."
        ]
    },
    "4": {
        "title": "📚 FASE 4: Sintesis Pustaka & Validasi Sitasi",
        "skills": "literature_review_generator, synthesize_research, citation_and_reference_validator, source_quality_appraiser",
        "items": [
            "**Citation Authenticity**: Metadata referensi (DOI, Penulis, Tahun, Jurnal) valid dan terverifikasi di Google Scholar/OpenAlex.",
            "**Source Quality**: Jurnal rujukan mayoritas terindeks di database bereputasi (Scopus Q1-Q2 / Web of Science).",
            "**No Hallucination**: Kutipan dan sintesis naskah sesuai secara kontekstual dengan isi paper asli tanpa fabrikasi."
        ]
    },
    "5": {
        "title": "📝 FASE 5: Peer Review, Revisi & Pemilihan Jurnal",
        "skills": "academic_peer_reviewer, reviewer_response_and_revision, journal_recommendation_finder, journal_template_formatter",
        "items": [
            "**Simulated Peer-Review**: Catatan kritik dari simulasi peer-review telah ditanggapi dan direvisi dalam naskah.",
            "**Target Journal & Author Guidelines**: Format draf naskah telah disesuaikan dengan template & panduan penulis jurnal sasaran.",
            "**FINAL HUMAN SIGN-OFF**: Peneliti menyetujui seluruh isi naskah dan mengonfirmasi kesiapan submit."
        ]
    }
}

def parse_args():
    parser = argparse.ArgumentParser(description="Master HITL Research Checklist Generator")
    parser.add_argument("--project-title", type=str, default="Penelitian Ilmiah", help="Title of the research project")
    parser.add_argument("--output", type=str, default="hitl_research_checklist.md", help="Output Markdown filepath")
    parser.add_argument("--active-phase", type=str, default="all", help="Active phase number (1-5 or 'all')")
    return parser.parse_args()

def generate_checklist(project_title, output_path, active_phase):
    now_str = datetime.date.today().isoformat()
    lines = [
        "# 🔬 Master Human-in-the-Loop (HITL) Research Evaluation Checklist",
        f"**Judul Riset / Proyek**: {project_title}  ",
        f"**Terakhir Diperbarui**: {now_str}  ",
        "**Koordinator Agent**: `research_orchestrator`  ",
        "**Status Workflow**: In Progress ⏳  ",
        "",
        "> [!IMPORTANT]",
        "> **Panduan Pengguna (Human Reviewer)**:",
        "> Silakan periksa setiap poin evaluasi di bawah ini setelah agent menyelesaikan fase riset terkait. Berikan tanda centang `[x]` pada item yang telah Anda divalidasi dan tulis catatan tambahan di bagian bawah bila diperlukan.",
        ""
    ]

    for p_id in sorted(PHASES.keys()):
        p_info = PHASES[p_id]
        status_badge = " (Siap Evaluasi 📌)" if (active_phase == "all" or active_phase == p_id) else ""
        lines.append(f"### {p_info['title']}{status_badge}")
        lines.append(f"*(Skills Terkait: `{p_info['skills']}`)*")
        for item in p_info["items"]:
            lines.append(f"- [ ] {item}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "### 📝 Catatan Evaluator & Instruksi Revisi (Human Sign-Off)",
        "**Status Persetujuan Akhir**:",
        "- [ ] **DRAFT APPROVED**: Peneliti menyetujui hasil alur kerja dan riset.",
        "- [ ] **REVISION REQUIRED**: Peneliti meminta agen melakukan penyesuaian/revisi.",
        "",
        "**Catatan Tambahan Peneliti**:",
        "> *(Tuliskan masukan, catatan kualitatif, atau instruksi penyesuaian khusus di sini)*",
        ""
    ])

    content = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"File HITL Research Evaluation Checklist berhasil dibuat/diperbarui: {os.path.abspath(output_path)}")

def main():
    args = parse_args()
    generate_checklist(args.project_title, args.output, args.active_phase)

if __name__ == "__main__":
    main()
