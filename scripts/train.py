from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a YOLOv8 model on the VisDrone dataset.")
    parser.add_argument("--data", required=True)
    parser.add_argument("--model", default="yolov8s.pt")
    parser.add_argument("--imgsz", type=int, default=1024)
    parser.add_argument("--epochs", type=int, default=80)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Training with data={args.data}, model={args.model}, imgsz={args.imgsz}, epochs={args.epochs}")


if __name__ == "__main__":
    main()