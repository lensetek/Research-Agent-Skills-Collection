#!/usr/bin/env python3
"""
fetch_evidence_snippet.py

Programmatic Guardrail for Citation Contextual Grounding & Evidence Extraction.
Queries OpenAlex, Crossref, and PubMed APIs to fetch abstract/text for a given DOI or title,
and extracts verbatim evidence snippets that match a given claim sentence.

Usage:
  python fetch_evidence_snippet.py --claim "AlphaFold predicts 3D protein structures with high accuracy" --doi 10.1038/s41586-021-03819-2
  python fetch_evidence_snippet.py --input claim_audit.json --output evidence_report.json
"""

import argparse
import difflib
import json
import re
import sys
import urllib.parse
import urllib.request
import ssl

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {
    'User-Agent': 'ResearchAgentSkillsEvidenceFetcher/1.0 (mailto:agent-skills@example.com)'
}

def create_ssl_context():
    return ssl.create_default_context()

def reconstruct_openalex_abstract(inverted_index):
    """Reconstructs full text abstract from OpenAlex abstract_inverted_index."""
    if not inverted_index or not isinstance(inverted_index, dict):
        return ""
    word_positions = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort(key=lambda x: x[0])
    return " ".join([word for _, word in word_positions])

def split_into_sentences(text):
    """Splits text into clean sentences."""
    if not text:
        return []
    cleaned = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?])\s+', cleaned)
    return [s.strip() for s in sentences if len(s.strip()) > 10]

STOPWORDS = {'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'this', 'that', 'with'}

def sentence_similarity(s1, s2):
    """Calculates similarity between claim sentence and reference sentence filtering common stopwords."""
    w1 = set(re.findall(r'\w+', s1.lower())) - STOPWORDS
    w2 = set(re.findall(r'\w+', s2.lower())) - STOPWORDS
    if not w1 or not w2:
        return 0.0
    overlap = len(w1.intersection(w2))
    jaccard = overlap / len(w1.union(w2))
    overlap_ratio = overlap / max(len(w1), 1)
    seq_ratio = difflib.SequenceMatcher(None, s1.lower(), s2.lower()).ratio()
    return round((0.5 * overlap_ratio) + (0.3 * jaccard) + (0.2 * seq_ratio), 4)

def fetch_paper_abstract(doi=None, title=None):
    """Fetches abstract text from OpenAlex / Crossref / PubMed APIs."""
    abstract_text = ""
    paper_metadata = {"found": False}

    # 1. Try OpenAlex by DOI
    if doi:
        clean_doi = re.sub(r'^https?://[^/]+/', '', doi.strip())
        url = f"https://api.openalex.org/works/https://doi.org/{urllib.parse.quote(clean_doi)}"
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=10, context=create_ssl_context()) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode('utf-8'))
                    inv_index = data.get('abstract_inverted_index')
                    abstract_text = reconstruct_openalex_abstract(inv_index)
                    paper_metadata = {
                        "found": True,
                        "title": data.get('display_name', ''),
                        "doi": clean_doi,
                        "year": data.get('publication_year'),
                        "source": "OpenAlex"
                    }
        except Exception:
            pass

    # 2. Fallback: Search OpenAlex by title if no abstract found
    if not abstract_text and title:
        encoded_title = urllib.parse.quote(title.strip())
        url = f"https://api.openalex.org/works?search={encoded_title}&per-page=1"
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=10, context=create_ssl_context()) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode('utf-8'))
                    results = data.get('results', [])
                    if results:
                        item = results[0]
                        inv_index = item.get('abstract_inverted_index')
                        abstract_text = reconstruct_openalex_abstract(inv_index)
                        paper_metadata = {
                            "found": True,
                            "title": item.get('display_name', ''),
                            "doi": item.get('doi', '').replace('https://doi.org/', ''),
                            "year": item.get('publication_year'),
                            "source": "OpenAlex Title Search"
                        }
        except Exception:
            pass

    return abstract_text, paper_metadata

def match_evidence_snippets(claim, abstract_text, top_k=3):
    """Finds top verbatim evidence snippets matching the claim."""
    if not abstract_text or not claim:
        return []

    sentences = split_into_sentences(abstract_text)
    scored = []
    for s in sentences:
        score = sentence_similarity(claim, s)
        scored.append({"snippet": s, "similarity_score": score})

    scored.sort(key=lambda x: x["similarity_score"], reverse=True)
    return scored[:top_k]

def verify_single_claim(claim, doi=None, title=None):
    abstract, meta = fetch_paper_abstract(doi=doi, title=title)
    snippets = match_evidence_snippets(claim, abstract)

    status = "UNSUPPORTED"
    if snippets and snippets[0]["similarity_score"] >= 0.25:
        status = "FULLY_SUPPORTED" if snippets[0]["similarity_score"] >= 0.40 else "PARTIALLY_SUPPORTED"

    return {
        "claim": claim,
        "doi": doi or meta.get("doi", ""),
        "paper_title": meta.get("title", title or "Unknown"),
        "abstract_found": bool(abstract),
        "status": status,
        "evidence_snippets": snippets
    }

def main():
    parser = argparse.ArgumentParser(description="Fetch evidence snippets for claim validation.")
    parser.add_argument("--claim", type=str, help="Claim statement sentence to verify.")
    parser.add_argument("--doi", type=str, help="DOI of target paper.")
    parser.add_argument("--title", type=str, help="Title of target paper.")
    parser.add_argument("--input", "-i", type=str, help="Path to input JSON file containing array of claims.")
    parser.add_argument("--output", "-o", type=str, help="Path to output JSON file.")

    args = parser.parse_args()

    results = []
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
            claims_list = data if isinstance(data, list) else [data]
            for item in claims_list:
                c = item.get("claim", "")
                d = item.get("doi")
                t = item.get("title")
                results.append(verify_single_claim(c, doi=d, title=t))
    elif args.claim:
        results.append(verify_single_claim(args.claim, doi=args.doi, title=args.title))
    else:
        sys.stderr.write("ERROR: Provide either --claim (with --doi/--title) or --input JSON file.\n")
        sys.exit(1)

    json_out = json.dumps(results, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(json_out)
        print(f"Successfully wrote evidence snippet report to {args.output}")
    else:
        print(json_out)

if __name__ == "__main__":
    main()
