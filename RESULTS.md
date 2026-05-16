# Results & Performance Metrics

## Model Performance (Validation Set)

| Metric | Value |
|--------|-------|
| mAP50 | 0.195 |
| mAP50-95 | 0.0983 |
| Human mAP50 | 0.0775 |
| Car mAP50 | 0.313 |
| Precision (Human) | 0.142 |
| Recall (Human) | 0.089 |
| Inference Speed | 1.5 fps (CPU) |
| Model Size | 22.5 MB |

## Dataset Processing Results

- ✓ 10,209 total images processed
- ✓ 6,471 training + 548 validation images converted  
- ✓ 3.13M object instances (1.49M humans, 1.64M cars)
- ✓ 100% validity rate

## Error Analysis

| Category | Count | Details |
|----------|-------|---------|
| False Positives | 45,670 | Shadows (40%), clutter (35%), reflections (15%) |
| False Negatives | 17,054 | Tiny objects (50%), occlusion (30%), blur (15%) |

## Inference Outputs

- 548 annotated images with bounding boxes and human count
- Predictions saved as JSONL format
- Per-image detection confidence scores
