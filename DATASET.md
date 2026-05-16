# VisDrone Human and Car Detection and Counting - Dataset Guide

**Download from Kaggle:**  
https://www.kaggle.com/datasets/banuprasadb/visdrone-dataset/versions/1?resource=download

## Dataset Statistics

| Split | Images | Labels |
|-------|--------|--------|
| Train | 6,471 | 6,471 |
| Val | 548 | 548 |
| Test-Dev | 1,610 | 1,610 |
| Test-Challenge | 1,580 | 1,580 |
| **Total** | **10,209** | **10,209** |

## Preparation

```bash
python scripts/prepare_dataset.py \
  --raw-dir /path/to/VisDrone_Dataset \
  --out-dir data/visdrone_yolo \
  --include-test --include-test-challenge
```

## Class Mapping

VisDrone 10 classes → Binary (Human, Car):
- HUMAN: pedestrian (1), people (2)
- CAR: car (4), van (5), truck (6), bus (7)
