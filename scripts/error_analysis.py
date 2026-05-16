from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze false positives and false negatives.")
    parser.add_argument("--weights", required=True)
    parser.add_argument("--yolo-dir", required=True)
    parser.add_argument("--split", default="val")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Error analysis placeholder for split={args.split} using {args.weights}")


if __name__ == "__main__":
    main()