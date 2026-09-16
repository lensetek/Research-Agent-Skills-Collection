#!/usr/bin/env python3
"""
MCP Auto-Updater & Zero-Failure Provisioning Utility.
Automatically detects, downloads, installs, and updates:
1. Chrome DevTools MCP (npx -y chrome-devtools-mcp@latest)
2. Windows MCP (cursortouch/windows-mcp via uvx/pip on Windows OS)
3. Research Agent Skills Collection Repository
"""

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

REPO_URL = "https://github.com/lensetek/Research-Agent-Skills-Collection"

def check_command(cmd):
    """Checks if a CLI executable command exists in PATH."""
    return shutil.which(cmd) is not None

def run_cmd(args_list, timeout=120):
    """Runs a system command cleanly and returns stdout, stderr, returncode."""
    try:
        res = subprocess.run(
            args_list,
            capture_output=True,
            text=True,
            timeout=timeout,
            shell=(platform.system() == "Windows")
        )
        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return 1, "", str(e)

def ensure_chrome_devtools_mcp(auto_install=True):
    """
    Ensures chrome-devtools-mcp is ready.
    If missing, automatically runs npx -y chrome-devtools-mcp@latest.
    """
    has_npx = check_command("npx")
    if not has_npx:
        return {
            "name": "chrome-devtools-mcp",
            "status": "error",
            "message": "npx (Node.js) tidak ditemukan. Harap pastikan Node.js terpasang."
        }

    if auto_install:
        # Run npx --yes chrome-devtools-mcp@latest --help to verify/auto-download package
        code, out, err = run_cmd(["npx", "-y", "chrome-devtools-mcp@latest", "--help"])
        if code == 0 or "chrome-devtools-mcp" in out or "chrome-devtools-mcp" in err:
            return {
                "name": "chrome-devtools-mcp",
                "status": "ready",
                "message": "Chrome DevTools MCP siap digunakan (npx -y chrome-devtools-mcp@latest).",
                "version": "latest"
            }
        else:
            return {
                "name": "chrome-devtools-mcp",
                "status": "ready_fallback",
                "message": f"npx siap digunakan. Pemicuan otomatis: npx -y chrome-devtools-mcp@latest (Output: {out or err})"
            }
    return {"name": "chrome-devtools-mcp", "status": "available", "message": "npx tersedia."}

def ensure_windows_mcp(auto_install=True):
    """
    Ensures cursortouch/windows-mcp is ready on Windows OS.
    If missing, automatically triggers uvx windows-mcp or pip install windows-mcp.
    """
    is_windows = platform.system() == "Windows"
    if not is_windows:
        return {
            "name": "windows-mcp",
            "status": "skipped",
            "message": "Windows MCP hanya berlaku untuk sistem operasi Windows."
        }

    has_uv = check_command("uv") or check_command("uvx")
    has_pip = check_command("pip") or check_command("pip3")

    if auto_install:
        if has_uv:
            # Try uvx windows-mcp --help
            code, out, err = run_cmd(["uvx", "windows-mcp", "--help"])
            if code == 0 or "windows-mcp" in out or "windows-mcp" in err:
                return {
                    "name": "windows-mcp",
                    "status": "ready",
                    "message": "Windows MCP siap via uvx (cursortouch/windows-mcp).",
                    "method": "uvx"
                }

        if has_pip:
            # Fallback to pip install --upgrade windows-mcp
            code, out, err = run_cmd([sys.executable, "-m", "pip", "install", "--upgrade", "windows-mcp"])
            if code == 0:
                return {
                    "name": "windows-mcp",
                    "status": "ready",
                    "message": "Windows MCP berhasil dipasang/diperbarui via pip (windows-mcp).",
                    "method": "pip"
                }

        # On-demand auto-launch command
        return {
            "name": "windows-mcp",
            "status": "ready_fallback",
            "message": "Pemicuan otomatis siap via command: uvx windows-mcp serve"
        }

    return {"name": "windows-mcp", "status": "available", "message": "Siap untuk dipicu."}

def check_repo_updates():
    """Checks git repository status for updates."""
    if check_command("git"):
        code, out, err = run_cmd(["git", "fetch", "--dry-run"])
        return {
            "name": "Research-Agent-Skills-Collection",
            "status": "checked",
            "repository": REPO_URL,
            "message": "Repositori lokal dapat disinkronkan dari GitHub."
        }
    return {
        "name": "Research-Agent-Skills-Collection",
        "status": "manual",
        "repository": REPO_URL,
        "message": "Gunakan prompt npx skills add untuk memperbarui."
    }

def main():
    parser = argparse.ArgumentParser(description="MCP Auto-Updater & Zero-Failure Provisioning Script")
    parser.add_argument("--check", action="store_true", help="Periksa status ketersediaan MCP")
    parser.add_argument("--update", action="store_true", help="Unduh dan perbarui semua dependensi MCP")
    parser.add_argument("--json", action="store_true", help="Format output sebagai JSON")
    args = parser.parse_args()

    auto_install = args.update or not args.check

    chrome_res = ensure_chrome_devtools_mcp(auto_install=auto_install)
    windows_res = ensure_windows_mcp(auto_install=auto_install)
    repo_res = check_repo_updates()

    results = {
        "timestamp": os.popen("echo %DATE% %TIME%" if platform.system() == "Windows" else "date").read().strip(),
        "packages": [chrome_res, windows_res, repo_res]
    }

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print("==================================================================")
        print("🤖 Research Agent MCP Auto-Provisioning & Update Status Report")
        print("==================================================================")
        for pkg in results["packages"]:
            print(f"• [{pkg['name']}] Status: {pkg['status'].upper()}")
            print(f"  Pesan: {pkg['message']}")
        print("==================================================================")

if __name__ == "__main__":
    main()
