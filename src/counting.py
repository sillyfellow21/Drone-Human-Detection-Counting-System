from __future__ import annotations


def count_humans_per_image(detections) -> int:
    count = 0
    for detection in detections or []:
        if int(detection.get("class_id", -1)) == 0:
            count += 1
    return count


def count_targets_per_image(detections) -> dict[str, int]:
    human_count = 0
    car_count = 0
    for detection in detections or []:
        class_id = int(detection.get("class_id", -1))
        if class_id == 0:
            human_count += 1
        elif class_id == 1:
            car_count += 1
    return {"human": human_count, "car": car_count}