from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize the prepared VisDrone dataset.")
    parser.add_argument("--yolo-dir", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=8)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Dataset directory: {args.yolo_dir}")
    print(f"Requested samples: {args.samples}")


if __name__ == "__main__":
    main()