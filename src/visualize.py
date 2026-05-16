from __future__ import annotations

from pathlib import Path

import cv2

from .config import TARGET_COLORS


def draw_bboxes(image, detections):
    canvas = image.copy()
    for detection in detections or []:
        x1, y1, x2, y2 = map(int, detection["bbox"])
        class_id = int(detection.get("class_id", 0))
        label = detection.get("label", str(class_id))
        score = float(detection.get("confidence", 0.0))
        color = TARGET_COLORS.get(class_id, (0, 255, 0))
        cv2.rectangle(canvas, (x1, y1), (x2, y2), color, 2)
        cv2.putText(canvas, f"{label} {score:.2f}", (x1, max(0, y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return canvas


def overlay_count(image, human_count: int):
    canvas = image.copy()
    cv2.putText(canvas, f"Humans: {human_count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    return canvas


def save_image(path: str | Path, image) -> None:
    cv2.imwrite(str(path), image)