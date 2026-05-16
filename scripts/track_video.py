from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Track detections in a video using ByteTrack.")
    parser.add_argument("--weights", required=True)
    parser.add_argument("--source", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Tracking placeholder for {args.source} using {args.weights}")


if __name__ == "__main__":
    main()