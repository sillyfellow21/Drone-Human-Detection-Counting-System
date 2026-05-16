from __future__ import annotations


def precision_recall(tp: int, fp: int, fn: int) -> tuple[float, float]:
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return precision, recall


def simple_detection_summary(predictions, ground_truths) -> dict[str, float]:
    tp = min(len(predictions or []), len(ground_truths or []))
    fp = max(0, len(predictions or []) - tp)
    fn = max(0, len(ground_truths or []) - tp)
    precision, recall = precision_recall(tp, fp, fn)
    return {"precision": precision, "recall": recall, "tp": tp, "fp": fp, "fn": fn}