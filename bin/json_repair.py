#!/usr/bin/env python3
"""
JSON Repair Utility for Agent LLM Outputs.
Handles markdown fence stripping, trailing comma fixes, quote fixes, and JSON extraction.
"""
import argparse
import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def clean_and_repair_json(text: str):
    """Attempt to extract and repair malformed JSON string from LLM output."""
    if not text or not text.strip():
        raise ValueError("Empty input string")

    cleaned = text.strip()

    # 1. Remove Markdown code fences (e.g. ```json ... ```)
    code_fence_pattern = r"```(?:json)?\s*(.*?)\s*```"
    match = re.search(code_fence_pattern, cleaned, re.DOTALL | re.IGNORECASE)
    if match:
        cleaned = match.group(1).strip()

    # 2. Extract first JSON object or array substring if wrapped in non-JSON text
    json_bounds_pattern = r"(\{.*\}|\[.*\])"
    bounds_match = re.search(json_bounds_pattern, cleaned, re.DOTALL)
    if bounds_match:
        cleaned = bounds_match.group(1).strip()

    # Try standard parse first
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # 3. Fix trailing commas before closing braces/brackets
    cleaned = re.sub(r",\s*([\}\]])", r"\1", cleaned)

    # 4. Try parsing again after trailing comma fix
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # 5. Fix single quotes to double quotes for keys/values (cautious replacement)
    # Replaces 'key': with "key":
    cleaned = re.sub(r"'([a-zA-Z0-9_\-\s]+)'\s*:", r'"\1":', cleaned)
    # Replaces : 'value' with : "value"
    cleaned = re.sub(r":\s*'([^']*)'", r': "\1"', cleaned)

    # Final attempt
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise ValueError(f"Unable to auto-repair JSON: {e}")

def main():
    parser = argparse.ArgumentParser(description="Repair malformed JSON from LLM output.")
    parser.add_argument("--input", "-i", type=str, help="Path to input text file containing LLM output.")
    parser.add_argument("--string", "-s", type=str, help="Raw string input.")
    parser.add_argument("--output", "-o", type=str, help="Output JSON file path (optional).")

    args = parser.parse_args()

    content = ""
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.string:
        content = args.string
    else:
        content = sys.stdin.read()

    try:
        data = clean_and_repair_json(content)
        json_out = json.dumps(data, indent=2, ensure_ascii=False)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(json_out)
            print(f"Successfully repaired JSON and wrote to {args.output}")
        else:
            print(json_out)
        sys.exit(0)
    except Exception as err:
        sys.stderr.write(f"ERROR: {err}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
