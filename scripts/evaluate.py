from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Optional

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate a YOLO weights file on a VisDrone-style dataset.")
    parser.add_argument("--weights", required=True, help="Path to model weights (pt)")
    parser.add_argument("--data", default="configs/visdrone_yolo.yaml", help="Path to dataset YAML (train/val/test paths)")
    parser.add_argument("--device", default="cpu", help="Device to run evaluation on (cpu or cuda)")
    parser.add_argument("--save-json", default=None, help="Optional path to save a JSON summary of metrics")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        from ultralytics import YOLO
    except Exception as e:  # pragma: no cover - dependency/runtime error
        raise SystemExit(f"ultralytics is required to run evaluation: {e}")

    print(f"Loading model: {args.weights}")
    model = YOLO(args.weights)

    print(f"Running validation on data: {args.data} (device={args.device})")
    metrics = model.val(data=args.data, device=args.device)

    # metrics is a DetMetrics object; mean_results returns [precision, recall, mAP50, mAP50-95]
    mean = metrics.mean_results() if hasattr(metrics, "mean_results") else []
    precision, recall, map50, map50_95 = (mean + [None, None, None, None])[:4]

    per_class_maps = None
    try:
        per_class_maps = metrics.maps.tolist() if hasattr(metrics, "maps") else None
    except Exception:
        per_class_maps = None

    names = metrics.names if hasattr(metrics, "names") else {}

    summary = {
        "precision": float(precision) if precision is not None else None,
        "recall": float(recall) if recall is not None else None,
        "mAP50": float(map50) if map50 is not None else None,
        "mAP50_95": float(map50_95) if map50_95 is not None else None,
        "per_class_maps": {int(k): float(v) for k, v in zip(names.keys(), per_class_maps)} if (per_class_maps is not None and names) else None,
    }

    print("\nEvaluation summary:")
    print(json.dumps(summary, indent=2))

    if args.save_json:
        out = Path(args.save_json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(summary, indent=2))
        print(f"Saved JSON summary to {out}")


if __name__ == "__main__":
    main()