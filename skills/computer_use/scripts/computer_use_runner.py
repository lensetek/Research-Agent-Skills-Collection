#!/usr/bin/env python3
"""
Computer Use Execution Helper & Auto-Fallback Manager.
Parses fallback references configuration and manages fallback recovery triggers.
"""

import argparse
import json
import os
import subprocess
import sys

FALLBACK_CONFIG = {
    "primary_skill": "stablyai/orca@computer-use",
    "fallback_references": [
        {
            "name": "web-infra-dev/midscene-skills@computer-automation",
            "type": "vision-based-ui",
            "command": "npx skills add web-infra-dev/midscene-skills@computer-automation"
        },
        {
            "name": "am-will/codex-skills@gemini-computer-use",
            "type": "gemini-optimized-schema",
            "command": "npx skills add am-will/codex-skills@gemini-computer-use"
        }
    ]
}

def parse_args():
    parser = argparse.ArgumentParser(description="Computer-Use Runner & Auto-Fallback Helper")
    parser.add_argument("--action", type=str, choices=["config", "check-fallback", "trigger-fallback"], default="config", help="Action to execute")
    parser.add_argument("--fallback-index", type=int, default=0, help="Index of fallback reference to trigger")
    return parser.parse_args()

def get_config():
    return json.dumps(FALLBACK_CONFIG, indent=2)

def trigger_fallback(index):
    if index < 0 or index >= len(FALLBACK_CONFIG["fallback_references"]):
        return json.dumps({"status": "error", "message": f"Invalid fallback index: {index}"})
    
    fallback = FALLBACK_CONFIG["fallback_references"][index]
    cmd = fallback["command"]
    
    print(f"Triggering auto-fallback to: {fallback['name']} ({fallback['type']})")
    print(f"Executing: {cmd}")
    
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        return json.dumps({
            "status": "success" if res.returncode == 0 else "failed",
            "fallback": fallback,
            "returncode": res.returncode,
            "stdout": res.stdout,
            "stderr": res.stderr
        }, indent=2)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "fallback": fallback,
            "message": str(e)
        }, indent=2)

def main():
    args = parse_args()
    if args.action == "config":
        print(get_config())
    elif args.action == "check-fallback":
        print(json.dumps({"fallback_count": len(FALLBACK_CONFIG["fallback_references"]), "references": FALLBACK_CONFIG["fallback_references"]}, indent=2))
    elif args.action == "trigger-fallback":
        print(trigger_fallback(args.fallback_index))

if __name__ == "__main__":
    main()
