from __future__ import annotations

import argparse
from pathlib import Path

import cv2
from ultralytics import YOLO


DEFAULT_SOURCE = Path("VisDrone_Dataset/VisDrone2019-DET-val/images")
DEFAULT_MODEL = Path("runs/detect/outputs/train/visdrone_yolo_cpu_tiny/weights/best.pt")
DEFAULT_OUTPUT = Path("results/demo_infer")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run image inference on a few VisDrone samples.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Directory with input images")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL, help="YOLO weights path")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT, help="Directory to save annotated images")
    parser.add_argument("--limit", type=int, default=5, help="Number of images to process")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    return parser.parse_args()


def resolve_model_path(model_path: Path) -> Path:
    if model_path.exists():
        return model_path
    fallback = Path("yolov8s.pt")
    if fallback.exists():
        return fallback
    raise FileNotFoundError(f"No model found at {model_path} or {fallback}")


def list_images(source_dir: Path, limit: int) -> list[Path]:
    if not source_dir.exists():
        raise FileNotFoundError(f"Image directory not found: {source_dir}")
    image_paths = sorted(
        [*source_dir.glob("*.jpg"), *source_dir.glob("*.jpeg"), *source_dir.glob("*.png")]
    )
    if not image_paths:
        raise FileNotFoundError(f"No images found in {source_dir}")
    return image_paths[:limit]


def count_people(result) -> int:
    person_like_names = {"person", "pedestrian", "people", "human"}
    names = result.names
    boxes = result.boxes
    if boxes is None or len(boxes) == 0:
        return 0
    count = 0
    for class_id in boxes.cls.tolist():
        class_name = names.get(int(class_id), str(int(class_id))) if isinstance(names, dict) else names[int(class_id)]
        if class_name.lower() in person_like_names or int(class_id) == 0:
            count += 1
    return count


def main() -> None:
    args = parse_args()
    model_path = resolve_model_path(args.model)
    image_paths = list_images(args.source, args.limit)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    model = YOLO(str(model_path))
    print(f"Using model: {model_path}")
    print(f"Input images: {len(image_paths)}")
    print(f"Output dir: {args.output_dir}")

    for image_path in image_paths:
        results = model.predict(source=str(image_path), conf=args.conf, device="cpu", verbose=False)
        result = results[0]
        annotated = result.plot()
        output_path = args.output_dir / image_path.name
        cv2.imwrite(str(output_path), annotated)
        person_count = count_people(result)
        print(f"{image_path.name}: detections={len(result.boxes) if result.boxes is not None else 0}, humans={person_count}, saved={output_path}")


if __name__ == "__main__":
    main()