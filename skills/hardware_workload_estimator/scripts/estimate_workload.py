#!/usr/bin/env python3
"""
Workload & Runtime Estimator script.
Calculates estimated execution time, memory footprint, and provides local vs cloud recommendation.
"""

import argparse
import json
import math
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Workload Estimator")
    parser.add_argument("--total-samples", type=int, default=10000, help="Total number of samples in dataset")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size used in training/inference")
    parser.add_argument("--epochs", type=int, default=10, help="Total epochs")
    parser.add_argument("--sample-time-sec", type=float, default=0.05, help="Measured time per batch in seconds")
    parser.add_argument("--sample-vram-mb", type=float, default=500.0, help="Measured VRAM per batch in MB")
    parser.add_argument("--available-vram-gb", type=float, default=4.0, help="Available VRAM in GB")
    parser.add_argument("--available-ram-gb", type=float, default=8.0, help="Available System RAM in GB")
    return parser.parse_args()

def main():
    args = parse_args()
    
    total_batches_per_epoch = math.ceil(args.total_samples / max(1, args.batch_size))
    total_batches_all = total_batches_per_epoch * args.epochs
    
    total_estimated_sec = round(total_batches_all * args.sample_time_sec, 2)
    total_estimated_min = round(total_estimated_sec / 60, 2)
    total_estimated_hr = round(total_estimated_min / 60, 2)
    
    vram_peak_gb = round(args.sample_vram_mb / 1024, 2)
    
    # Recommendation Logic
    recommendation = "RECOMMENDED_LOCAL"
    reasons = []
    
    if total_estimated_min > 20:
        recommendation = "RECOMMENDED_CLOUD_COLAB"
        reasons.append(f"Estimated training time ({total_estimated_min} minutes) exceeds 20 minutes threshold for local machine.")
    
    if vram_peak_gb > (args.available_vram_gb * 0.85):
        recommendation = "RECOMMENDED_CLOUD_COLAB"
        reasons.append(f"Peak memory estimation ({vram_peak_gb} GB) exceeds 85% of available VRAM ({args.available_vram_gb} GB). Risk of OOM.")

    if not reasons:
        reasons.append("Training time and VRAM footprint are well within local hardware capacity.")

    output = {
        "workload_params": {
            "total_samples": args.total_samples,
            "batch_size": args.batch_size,
            "epochs": args.epochs,
            "total_batches": total_batches_all
        },
        "estimation": {
            "total_seconds": total_estimated_sec,
            "total_minutes": total_estimated_min,
            "total_hours": total_estimated_hr,
            "estimated_vram_gb": vram_peak_gb
        },
        "recommendation": recommendation,
        "reasons": reasons
    }
    
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
