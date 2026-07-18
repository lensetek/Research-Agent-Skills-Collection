#!/usr/bin/env python3
"""
Progress Tracker Utility for Research Agent 5-Phase Workflow.
Manages progress.json state file to maintain execution state for LLM agents.
"""
import argparse
import datetime
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PROGRESS_FILE = "progress.json"

DEFAULT_PHASES = {
    1: {"name": "Discovery & Framing", "skills": ["discover-phenomenon-and-gap", "research-question-builder", "hypothesis-or-proposition-builder"]},
    2: {"name": "Research Methodology & Experiments", "skills": ["research-design-planner", "synthetic-data-generator", "data-acquisition-specialist", "data-scientist-analyst", "model-evaluator-validator"]},
    3: {"name": "Literature Intelligence & Audit", "skills": ["literature-review-generator", "extract-methodology", "source-quality-appraiser", "citation-and-reference-validator", "paper-matrix-builder"]},
    4: {"name": "Synthesis & Publication Readiness", "skills": ["synthesize-research", "patent-and-literature-matcher", "journal-recommendation-finder", "journal-template-formatter", "academic-peer-reviewer", "obsidian-vault-exporter"]},
    5: {"name": "Personalization & Profile Memory", "skills": ["user_profile.json update"]}
}

def load_progress(filepath=PROGRESS_FILE):
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def save_progress(data, filepath=PROGRESS_FILE):
    data["updated_at"] = datetime.datetime.now().isoformat()
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def cmd_init(args):
    data = {
        "topic": args.topic,
        "mode": args.mode,
        "created_at": datetime.datetime.now().isoformat(),
        "updated_at": datetime.datetime.now().isoformat(),
        "current_phase": 1,
        "phase_name": DEFAULT_PHASES[1]["name"],
        "completed_phases": [],
        "skill_history": [],
        "artifacts_generated": []
    }
    save_progress(data)
    print(f"Initialized research progress for topic: '{args.topic}' (Mode: {args.mode})")

def cmd_update(args):
    data = load_progress()
    if not data:
        sys.stderr.write("ERROR: progress.json not found. Run init first.\n")
        sys.exit(1)

    if args.phase:
        data["current_phase"] = args.phase
        data["phase_name"] = DEFAULT_PHASES.get(args.phase, {}).get("name", f"Phase {args.phase}")

    skill_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "phase": data["current_phase"],
        "skill": args.skill,
        "status": args.status,
        "notes": args.notes or ""
    }
    data["skill_history"].append(skill_entry)

    if args.artifact:
        if args.artifact not in data["artifacts_generated"]:
            data["artifacts_generated"].append(args.artifact)

    save_progress(data)
    print(f"Updated progress: Phase {data['current_phase']} | Skill: {args.skill} | Status: {args.status}")

def cmd_show(args):
    data = load_progress()
    if not data:
        print("No active progress.json found.")
        sys.exit(0)
    print(json.dumps(data, indent=2, ensure_ascii=False))

def cmd_advance(args):
    data = load_progress()
    if not data:
        sys.stderr.write("ERROR: progress.json not found. Run init first.\n")
        sys.exit(1)

    curr = data.get("current_phase", 1)
    if curr not in data["completed_phases"]:
        data["completed_phases"].append(curr)

    next_p = curr + 1
    if next_p in DEFAULT_PHASES:
        data["current_phase"] = next_p
        data["phase_name"] = DEFAULT_PHASES[next_p]["name"]
        print(f"Advanced to Phase {next_p}: {DEFAULT_PHASES[next_p]['name']}")
    else:
        print(f"All 5 phases completed!")

    save_progress(data)

def main():
    parser = argparse.ArgumentParser(description="Progress Tracker CLI for Research Agent Workflow.")
    subparsers = parser.add_subparsers(dest="subcommand", help="Sub-command help")

    # init
    p_init = subparsers.add_parser("init", help="Initialize progress.json")
    p_init.add_argument("--topic", "-t", required=True, help="Research topic")
    p_init.add_argument("--mode", "-m", default="Literature-Driven", choices=["Literature-Driven", "Dataset-Driven"], help="Research mode")

    # update
    p_up = subparsers.add_parser("update", help="Update skill execution status")
    p_up.add_argument("--skill", "-s", required=True, help="Name of executed skill")
    p_up.add_argument("--status", type=str, default="COMPLETED", choices=["COMPLETED", "FAILED", "IN_PROGRESS"], help="Status")
    p_up.add_argument("--phase", "-p", type=int, help="Override current phase number")
    p_up.add_argument("--notes", "-n", help="Notes or summary")
    p_up.add_argument("--artifact", "-a", help="Generated artifact filename or path")

    # show
    p_show = subparsers.add_parser("show", help="Display progress.json")

    # advance
    p_adv = subparsers.add_parser("advance", help="Advance to next phase")

    args = parser.parse_args()

    if args.subcommand == "init":
        cmd_init(args)
    elif args.subcommand == "update":
        cmd_update(args)
    elif args.subcommand == "show":
        cmd_show(args)
    elif args.subcommand == "advance":
        cmd_advance(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
