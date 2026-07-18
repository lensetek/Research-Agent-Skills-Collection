#!/usr/bin/env python3
"""
Section Extraction Utility for Extract-Methodology Skill.
Parses paper text/markdown and extracts Methodology, Experimental Setup, Results, and Parameters sections.
Pre-filters text to prevent prompt bloat and context degradation in LLMs.
"""
import argparse
import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SECTION_PATTERNS = {
    "methodology": r"(?:#+|\b)(?:methodology|methods|proposed method|architecture|model)\b(.*?)(?=\n#+|\b(?:experimental setup|experiments|results|discussion|conclusion)\b|\Z)",
    "experiments": r"(?:#+|\b)(?:experimental setup|experiment setup|experiments|dataset|implementation details)\b(.*?)(?=\n#+|\b(?:results|discussion|conclusion)\b|\Z)",
    "results": r"(?:#+|\b)(?:results|evaluation|performance|experimental results)\b(.*?)(?=\n#+|\b(?:discussion|related work|conclusion|references)\b|\Z)"
}

def extract_sections_from_text(text: str) -> dict:
    results = {}
    for section_name, pattern in SECTION_PATTERNS.items():
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        if matches:
            # Combine matches and trim excessive whitespace
            extracted = "\n---\n".join([m.strip() for m in matches if m.strip()])
            results[section_name] = extracted[:4000] # Cap at 4000 chars per section
        else:
            results[section_name] = "Section not explicitly found in text snippet."
    return results

def process_file(filepath: str) -> dict:
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    filename = os.path.basename(filepath)
    extracted = extract_sections_from_text(content)
    extracted["source_file"] = filename
    return extracted

def main():
    parser = argparse.ArgumentParser(description="Extract technical sections (Methodology, Setup, Results) from paper texts.")
    parser.add_argument("--input", "-i", required=True, help="Path to paper text/markdown file or directory.")
    parser.add_argument("--output", "-o", help="Output JSON filepath.")

    args = parser.parse_args()

    results = []
    if os.path.isdir(args.input):
        for fname in sorted(os.listdir(args.input)):
            if fname.endswith((".txt", ".md", ".json")):
                fpath = os.path.join(args.input, fname)
                results.append(process_file(fpath))
    elif os.path.isfile(args.input):
        results.append(process_file(args.input))
    else:
        sys.stderr.write(f"ERROR: Input path {args.input} does not exist.\n")
        sys.exit(1)

    json_output = json.dumps(results, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(json_output)
        print(f"Successfully extracted sections for {len(results)} paper(s) to {args.output}")
    else:
        print(json_output)

if __name__ == "__main__":
    main()
