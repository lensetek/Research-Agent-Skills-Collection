#!/usr/bin/env python3
"""
validate_references.py

Programmatic Guardrail for Citation & Reference Validation.
Queries Crossref and OpenAlex public APIs to verify the authenticity of references,
DOIs, titles, authors, and publication years without requiring API keys.

Usage:
  python validate_references.py --input references.json --output report.json
  python validate_references.py --doi 10.1038/s41586-021-03819-2
  python validate_references.py --title "Highly accurate protein structure prediction with AlphaFold"
"""

import argparse
import difflib
import json
import re
import sys
import urllib.parse
import urllib.request
import ssl

HEADERS = {
    'User-Agent': 'ResearchAgentSkillsValidator/1.0 (mailto:agent-skills@example.com)'
}

def create_ssl_context():
    context = ssl.create_default_context()
    return context

def title_similarity(t1: str, t2: str) -> float:
    """Computes similarity ratio between two titles after normalizing whitespace and punctuation."""
    def clean(s):
        return re.sub(r'[^\w\s]', '', s.lower()).strip()
    return difflib.SequenceMatcher(None, clean(t1), clean(t2)).ratio()

def query_crossref_doi(doi: str):
    """Fetch metadata for a DOI from Crossref REST API."""
    clean_doi = doi.strip()
    if clean_doi.startswith("http"):
        clean_doi = re.sub(r'^https?://[^/]+/', '', clean_doi)
    
    url = f"https://api.crossref.org/works/{urllib.parse.quote(clean_doi)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10, context=create_ssl_context()) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                item = data.get('message', {})
                titles = item.get('title', [])
                title = titles[0] if titles else ""
                
                authors = []
                for a in item.get('author', []):
                    given = a.get('given', '')
                    family = a.get('family', '')
                    authors.append(f"{given} {family}".strip())
                
                year = None
                pub_date = item.get('issued', {}).get('date-parts', [[]])[0]
                if pub_date:
                    year = pub_date[0]
                
                return {
                    'found': True,
                    'title': title,
                    'authors': authors,
                    'year': year,
                    'doi': clean_doi,
                    'publisher': item.get('publisher', ''),
                    'source': 'Crossref'
                }
    except Exception:
        pass
    return {'found': False, 'doi': clean_doi}

def query_openalex_title(title: str):
    """Search OpenAlex for a paper title."""
    if not title or len(title.strip()) < 5:
        return {'found': False}
    
    encoded_title = urllib.parse.quote(title.strip())
    url = f"https://api.openalex.org/works?search={encoded_title}&per-page=3"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10, context=create_ssl_context()) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                results = data.get('results', [])
                for res in results:
                    found_title = res.get('display_name', '')
                    sim = title_similarity(title, found_title)
                    if sim >= 0.70:
                        authors = [a.get('author', {}).get('display_name', '') for a in res.get('authorships', [])]
                        year = res.get('publication_year')
                        doi = res.get('doi', '').replace('https://doi.org/', '') if res.get('doi') else ''
                        return {
                            'found': True,
                            'title': found_title,
                            'authors': authors,
                            'year': year,
                            'doi': doi,
                            'similarity': sim,
                            'source': 'OpenAlex'
                        }
    except Exception:
        pass
    return {'found': False}

def validate_single_reference(ref: dict) -> dict:
    """Validates a reference object containing title, authors, year, doi."""
    given_doi = ref.get('doi', '')
    given_title = ref.get('title', '')

    result = {
        'input': ref,
        'status': 'HALLUCINATED',
        'details': 'No matching metadata found in OpenAlex or Crossref.',
        'match': None
    }

    # 1. Try DOI lookup if provided
    if given_doi:
        crossref_res = query_crossref_doi(given_doi)
        if crossref_res.get('found'):
            match_title = crossref_res.get('title', '')
            sim = title_similarity(given_title, match_title) if given_title else 1.0
            
            if sim >= 0.65 or not given_title:
                result['status'] = 'VALID'
                result['details'] = f"DOI verified via Crossref. Title similarity: {sim:.2f}"
                result['match'] = crossref_res
                return result
            else:
                result['status'] = 'METADATA_MISMATCH'
                result['details'] = f"DOI exists on Crossref, but title differs significantly. Given: '{given_title}', Found: '{match_title}'"
                result['match'] = crossref_res
                return result

    # 2. Try Title search if DOI not provided or failed
    if given_title:
        openalex_res = query_openalex_title(given_title)
        if openalex_res.get('found'):
            sim = openalex_res.get('similarity', 0.0)
            result['status'] = 'VALID'
            result['details'] = f"Matched via OpenAlex title search. Similarity: {sim:.2f}"
            result['match'] = openalex_res
            return result

    return result

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    parser = argparse.ArgumentParser(description="Validate references against Crossref and OpenAlex APIs.")
    parser.add_argument('--input', help="Path to JSON file containing a list of reference objects.")
    parser.add_argument('--output', help="Path to save output JSON report.")
    parser.add_argument('--doi', help="Single DOI to validate.")
    parser.add_argument('--title', help="Single paper title to search and validate.")
    
    args = parser.parse_args()

    entries = []
    if args.doi:
        entries.append({'doi': args.doi, 'title': args.title or ''})
    elif args.title:
        entries.append({'title': args.title})
    elif args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                entries = data
            elif isinstance(data, dict) and 'references' in data:
                entries = data['references']
    else:
        if not sys.stdin.isatty():
            try:
                data = json.load(sys.stdin)
                if isinstance(data, list):
                    entries = data
                elif isinstance(data, dict) and 'references' in data:
                    entries = data['references']
            except Exception:
                pass

    if not entries:
        print(json.dumps({'error': 'No input references provided. Use --input, --doi, --title, or pipe JSON to stdin.'}, indent=2))
        sys.exit(1)

    results = []
    valid_count = 0
    hallucinated_count = 0
    mismatch_count = 0

    for idx, ref in enumerate(entries):
        val = validate_single_reference(ref)
        results.append(val)
        if val['status'] == 'VALID':
            valid_count += 1
        elif val['status'] == 'HALLUCINATED':
            hallucinated_count += 1
        else:
            mismatch_count += 1

    summary = {
        'total': len(entries),
        'valid': valid_count,
        'hallucinated': hallucinated_count,
        'metadata_mismatch': mismatch_count,
        'results': results
    }

    output_json = json.dumps(summary, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_json)
        print(f"Validation report saved to {args.output}")
    else:
        print(output_json)

if __name__ == '__main__':
    main()
