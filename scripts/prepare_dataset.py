from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare VisDrone data in YOLO format.")
    parser.add_argument("--raw-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--include-test", action="store_true")
    parser.add_argument("--include-test-challenge", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Prepared output directory: {args.out_dir}")
    print(f"Raw dataset: {args.raw_dir}")


if __name__ == "__main__":
    main()