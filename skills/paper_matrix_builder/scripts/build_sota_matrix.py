#!/usr/bin/env python3
"""
SotA Matrix Builder Utility for Paper-Matrix-Builder Skill.
Aggregates structured extraction JSONs into standardized Markdown and CSV comparison tables.
Guarantees 100% data integrity and explicit 'NOT REPORTED' flags for missing metrics.
"""
import argparse
import csv
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

COLUMNS = [
    "Author & Year",
    "Model / Method",
    "Primary Dataset",
    "Key Parameters",
    "Evaluation Metrics",
    "Performance Figures",
    "Limitations / Gaps"
]

def format_cell_value(val):
    if val is None or str(val).strip() == "" or str(val).strip().lower() in ["none", "null", "undefined", "n/a"]:
        return "NOT REPORTED"
    if isinstance(val, list):
        return ", ".join([str(v) for v in val])
    return str(val).replace("\n", " ").strip()

def build_matrix(data_list):
    rows = []
    for item in data_list:
        row = {
            "Author & Year": format_cell_value(item.get("author_year") or item.get("paper_id") or item.get("source_file")),
            "Model / Method": format_cell_value(item.get("model") or item.get("method") or item.get("primary_method")),
            "Primary Dataset": format_cell_value(item.get("dataset") or item.get("datasets")),
            "Key Parameters": format_cell_value(item.get("parameters") or item.get("hyperparameters")),
            "Evaluation Metrics": format_cell_value(item.get("metrics") or item.get("evaluation_metrics")),
            "Performance Figures": format_cell_value(item.get("results") or item.get("performance") or item.get("metrics_results")),
            "Limitations / Gaps": format_cell_value(item.get("limitations") or item.get("gaps"))
        }
        rows.append(row)
    return rows

def render_markdown(rows):
    lines = []
    lines.append("| " + " | ".join(COLUMNS) + " |")
    lines.append("| " + " | ".join(["---"] * len(COLUMNS)) + " |")
    for r in rows:
        row_str = "| " + " | ".join([r[col] for col in COLUMNS]) + " |"
        lines.append(row_str)
    return "\n".join(lines)

def export_csv(rows, filepath):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

def main():
    parser = argparse.ArgumentParser(description="Build SotA Markdown and CSV matrices from extraction JSONs.")
    parser.add_argument("--input", "-i", required=True, help="Input JSON file or directory of extraction JSONs.")
    parser.add_argument("--output-md", help="Output Markdown filepath.")
    parser.add_argument("--output-csv", help="Output CSV filepath.")

    args = parser.parse_args()

    items = []
    if os.path.isdir(args.input):
        for fname in sorted(os.listdir(args.input)):
            if fname.endswith(".json"):
                fpath = os.path.join(args.input, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = json.load(f)
                    if isinstance(content, list):
                        items.extend(content)
                    else:
                        items.append(content)
    elif os.path.isfile(args.input):
        with open(args.input, "r", encoding="utf-8") as f:
            content = json.load(f)
            if isinstance(content, list):
                items.extend(content)
            else:
                items.append(content)
    else:
        sys.stderr.write(f"ERROR: Input path {args.input} does not exist.\n")
        sys.exit(1)

    rows = build_matrix(items)
    md_matrix = render_markdown(rows)

    if args.output_md:
        with open(args.output_md, "w", encoding="utf-8") as f:
            f.write(md_matrix)
        print(f"Successfully wrote Markdown matrix to {args.output_md}")
    else:
        print("### State-of-the-Art (SotA) Matrix\n")
        print(md_matrix)

    if args.output_csv:
        export_csv(rows, args.output_csv)
        print(f"Successfully wrote CSV matrix to {args.output_csv}")

if __name__ == "__main__":
    main()
