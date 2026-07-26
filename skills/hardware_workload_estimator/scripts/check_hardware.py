#!/usr/bin/env python3
"""
Diagnostic script to check local hardware specs (CPU, System RAM, GPU/VRAM).
Outputs structured JSON for agent processing.
"""

import json
import os
import platform
import sys

def get_cpu_info():
    info = {
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_count_logical": os.cpu_count() or 1,
        "cpu_count_physical": os.cpu_count() or 1
    }
    try:
        import psutil
        info["cpu_count_physical"] = psutil.cpu_count(logical=False) or info["cpu_count_logical"]
        info["cpu_percent"] = psutil.cpu_percent(interval=0.1)
    except ImportError:
        pass
    return info

def get_ram_info():
    info = {
        "total_gb": None,
        "available_gb": None,
        "used_percent": None
    }
    try:
        import psutil
        mem = psutil.virtual_memory()
        info["total_gb"] = round(mem.total / (1024**3), 2)
        info["available_gb"] = round(mem.available / (1024**3), 2)
        info["used_percent"] = mem.percent
    except ImportError:
        # Fallback for Windows/Linux if psutil is missing
        if sys.platform == "win32":
            try:
                import ctypes
                class MEMORYSTATUSEX(ctypes.Structure):
                    _fields_ = [
                        ('dwLength', ctypes.c_ulong),
                        ('dwMemoryLoad', ctypes.c_ulong),
                        ('ullTotalPhys', ctypes.c_ulonglong),
                        ('ullAvailPhys', ctypes.c_ulonglong),
                        ('ullTotalPageFile', ctypes.c_ulonglong),
                        ('ullAvailPageFile', ctypes.c_ulonglong),
                        ('ullTotalVirtual', ctypes.c_ulonglong),
                        ('ullAvailVirtual', ctypes.c_ulonglong),
                        ('sullAvailExtendedVirtual', ctypes.c_ulonglong),
                    ]
                stat = MEMORYSTATUSEX()
                stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
                ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
                info["total_gb"] = round(stat.ullTotalPhys / (1024**3), 2)
                info["available_gb"] = round(stat.ullAvailPhys / (1024**3), 2)
                info["used_percent"] = float(stat.dwMemoryLoad)
            except Exception:
                pass
    return info

def get_gpu_info():
    gpus = []
    has_cuda = False
    has_mps = False
    
    try:
        import torch
        if torch.cuda.is_available():
            has_cuda = True
            for i in range(torch.cuda.device_count()):
                props = torch.cuda.get_device_properties(i)
                total_vram_gb = round(props.total_memory / (1024**3), 2)
                allocated_gb = round(torch.cuda.memory_allocated(i) / (1024**3), 2)
                reserved_gb = round(torch.cuda.memory_reserved(i) / (1024**3), 2)
                gpus.append({
                    "id": i,
                    "name": props.name,
                    "type": "CUDA",
                    "total_vram_gb": total_vram_gb,
                    "available_vram_gb": round(total_vram_gb - reserved_gb, 2),
                    "allocated_vram_gb": allocated_gb,
                    "compute_capability": f"{props.major}.{props.minor}"
                })
        
        if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            has_mps = True
            gpus.append({
                "id": 0,
                "name": "Apple Metal Performance Shaders (MPS)",
                "type": "MPS",
                "total_vram_gb": "Unified Memory",
                "available_vram_gb": "Unified Memory"
            })
    except ImportError:
        pass
    
    # Fallback to nvidia-smi command if torch is not installed or CUDA is false
    if not gpus and sys.platform in ["win32", "linux", "linux2"]:
        try:
            import subprocess
            cmd = ["nvidia-smi", "--query-gpu=index,name,memory.total,memory.free", "--format=csv,noheader,nounits"]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=3)
            if res.returncode == 0:
                for line in res.stdout.strip().split("\n"):
                    if line.strip():
                        parts = [p.strip() for p in line.split(",")]
                        if len(parts) >= 4:
                            gpus.append({
                                "id": int(parts[0]),
                                "name": parts[1],
                                "type": "CUDA (nvidia-smi)",
                                "total_vram_gb": round(float(parts[2]) / 1024, 2),
                                "available_vram_gb": round(float(parts[3]) / 1024, 2)
                            })
        except Exception:
            pass

    return {
        "gpu_count": len(gpus),
        "has_cuda": has_cuda or any(g["type"].startswith("CUDA") for g in gpus),
        "has_mps": has_mps,
        "devices": gpus
    }

def main():
    report = {
        "platform": platform.platform(),
        "system": platform.system(),
        "python_version": sys.version.split()[0],
        "cpu": get_cpu_info(),
        "ram": get_ram_info(),
        "gpu": get_gpu_info()
    }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
