from __future__ import annotations


def extract_tracks(detections):
    return [{**detection, "track_id": index} for index, detection in enumerate(detections or [], start=1)]


def draw_tracks(image, tracks):
    return image