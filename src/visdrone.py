from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class VisDroneDataset:
    root: Path

    def image_dir(self, split: str) -> Path:
        return self.root / f"VisDrone2019-DET-{split}" / "images"

    def label_dir(self, split: str) -> Path:
        return self.root / f"VisDrone2019-DET-{split}" / "labels"


def parse_annotations(path: str | Path) -> list[tuple[int, int, int, int, int, int, int, int]]:
    annotations = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            values = [int(float(part)) for part in line.strip().split(",") if part]
            if len(values) == 8:
                annotations.append(tuple(values))
    return annotations


def filter_and_map_boxes(annotations):
    mapped = []
    for x, y, w, h, score, category, truncation, occlusion in annotations:
        if category in {1, 2, 4, 5, 6, 7} and score > 0:
            mapped.append((x, y, w, h, category))
    return mapped