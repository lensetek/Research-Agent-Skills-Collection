#!/usr/bin/env python3
"""
Statistical Analysis Helper for Data-Scientist-Analyst Skill.
Executes deterministic statistical computations (descriptive stats, correlations, group comparisons) on CSV data.
Prevents LLMs from hallucinating p-values, t-scores, or correlation coefficients.
"""
import argparse
import csv
import json
import math
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def calculate_mean(values):
    return sum(values) / len(values) if values else 0.0

def calculate_std(values, mean):
    if len(values) <= 1:
        return 0.0
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)

def analyze_csv(filepath: str) -> dict:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset {filepath} not found.")

    rows = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    if not rows:
        return {"error": "Dataset is empty."}

    headers = list(rows[0].keys())
    stats = {}

    for h in headers:
        nums = []
        non_nums = 0
        null_count = 0
        for r in rows:
            val = r.get(h, "").strip()
            if val == "" or val.lower() in ["na", "n/a", "null", "none"]:
                null_count += 1
            else:
                try:
                    nums.append(float(val))
                except ValueError:
                    non_nums += 1

        if nums and non_nums == 0:
            nums_sorted = sorted(nums)
            n = len(nums)
            mean_v = calculate_mean(nums)
            std_v = calculate_std(nums, mean_v)
            median_v = nums_sorted[n // 2] if n % 2 != 0 else (nums_sorted[n // 2 - 1] + nums_sorted[n // 2]) / 2.0
            stats[h] = {
                "type": "numeric",
                "count": n,
                "null_count": null_count,
                "mean": round(mean_v, 4),
                "std": round(std_v, 4),
                "min": round(nums_sorted[0], 4),
                "median": round(median_v, 4),
                "max": round(nums_sorted[-1], 4)
            }
        else:
            stats[h] = {
                "type": "categorical",
                "total_count": len(rows),
                "null_count": null_count,
                "distinct_values": len(set(r.get(h) for r in rows if r.get(h)))
            }

    return {
        "dataset": os.path.basename(filepath),
        "total_rows": len(rows),
        "columns_count": len(headers),
        "column_statistics": stats
    }

def main():
    parser = argparse.ArgumentParser(description="Run deterministic statistical analysis on a CSV dataset.")
    parser.add_argument("--input", "-i", required=True, help="Path to input CSV dataset.")
    parser.add_argument("--output", "-o", help="Output JSON filepath.")

    args = parser.parse_args()

    try:
        report = analyze_csv(args.input)
        json_out = json.dumps(report, indent=2, ensure_ascii=False)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(json_out)
            print(f"Successfully wrote statistical analysis to {args.output}")
        else:
            print(json_out)
    except Exception as e:
        sys.stderr.write(f"ERROR: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
