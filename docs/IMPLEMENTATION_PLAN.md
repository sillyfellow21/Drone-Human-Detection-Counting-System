# Implementation Plan & Architecture

## System Architecture

```
VisDrone Images (10K)
    ↓ prepare_dataset.py
YOLO Format (train/val/test)
    ↓ train.py
YOLOv8s Weights (22.5MB)
    ↓ infer_images.py
Detections + Counts (548 images)
    ↓ error_analysis.py
FP/FN Categorization (45.6K + 17.1K)
```

## Core Modules

### src/visdrone.py
- Parse VisDrone CSV annotations
- Filter to binary classes (HUMAN, CAR)
- Convert to YOLO format
- Handle ignored regions and invalid boxes

### src/counting.py
- Count detections by class_id=0 (humans)
- Apply confidence threshold filtering
- Return per-image counts

### src/visualize.py
- Draw bounding boxes with class labels
- Overlay confidence scores
- Display human count on annotated images

### src/evaluation.py
- Compute precision, recall, mAP
- Per-class performance metrics
- Confusion matrices

### src/tracking.py
- ByteTrack integration (optional)
- Track IDs across frames
- Modular design (works with or without)

## Key Design Decisions

1. **Binary Classification**: Reduced VisDrone's 10 classes to 2 (focused detection)
2. **Transfer Learning**: YOLOv8s pretrained on COCO (349/355 weights transferred)
3. **Modular Architecture**: Reusable library code in src/, orchestration in scripts/
4. **Fixed Seed (42)**: Reproducible results across runs
5. **Error Categorization**: Root-cause analysis beyond aggregated metrics
