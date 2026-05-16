from __future__ import annotations

from pathlib import Path
from typing import Iterable


def ensure_dir(path: str | Path) -> Path:
    resolved = Path(path)
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def list_images(folder: str | Path) -> list[Path]:
    base = Path(folder)
    if not base.exists():
        return []
    return sorted([*base.glob("*.jpg"), *base.glob("*.jpeg"), *base.glob("*.png")])


def chunked(items: Iterable, size: int):
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch