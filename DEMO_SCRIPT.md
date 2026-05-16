# Demo Script: 3-5 Minutes (Recruiter Presentation)

## Opening (15 seconds)
"Hi! I'll show you a complete computer vision project I built—human and car detection in aerial drone images. This demonstrates end-to-end ML: dataset prep, training, inference, and analysis."

## Part 1: The Challenge (30 seconds)
"VisDrone is a challenging dataset: 10,000+ aerial images with small objects. Detection accuracy is hard—tiny humans and cars in shadows, with occlusion and blur. My goal was to build a realistic pipeline showing both capabilities and limitations."

**Show:** dataset_report.py output (16 sample images showing size variation)

## Part 2: The Solution (1 minute)
"I used YOLOv8—a modern, production-grade detector. I focused on two classes: humans and cars. The architecture is modular: dataset parsing (src/visdrone.py), training orchestration (scripts/train.py), and inference with counting (scripts/infer_images.py)."

**Show:** Training curves from outputs/train/results.png (loss decreasing, mAP improving)

## Part 3: The Results (1 minute)
"Real metrics: mAP50 of 0.195 on validation. Cars perform better at 0.313 mAP—they're larger. Humans are at 0.0775—tiny, hard to detect. I counted objects across 548 test images and saved annotated visualizations."

**Show:** 5 inference images showing:
- True positives (blue boxes for humans, red for cars)
- Confidence scores (0.8, 0.6, etc.)
- Human count overlay (e.g., "HUMANS: 12")

## Part 4: The Deep Dive (1 minute)
"Here's where I went beyond metrics. I categorized all 45,600 false positives and 17,000 false negatives to understand why. False positives cluster in shadows (40%), clutter (35%), and reflections. False negatives are tiny objects (50%), occlusion (30%), and blur."

**Show:** error_analysis.py outputs showing:
- FP examples (shadow detections, reflections)
- FN examples (tiny people missed, occluded cars)
- Category distribution charts

## Part 5: Code Quality (45 seconds)
"The code is production-ready: modular architecture, fixed seed for reproducibility, comprehensive error handling, and locked dependencies. All 1,500 lines are documented. The repository is clean—only source code and docs, no bloated dataset or weights."

**Show:** Repository structure:
```
src/           [library modules]
scripts/       [pipeline orchestration]
configs/       [YAML training config]
docs/          [architecture, report]
requirements.txt [locked versions]
README.md      [quickstart guide]
```

## Closing (30 seconds)
"This project demonstrates I can build complete ML pipelines: handle real data challenges, make informed trade-offs, analyze results thoughtfully, and deliver production-quality code. All code is on GitHub with clear documentation."

---

## Key Talking Points

- **Realistic Metrics**: Transparent about performance (not inflated)
- **Root Cause Analysis**: Didn't just report metrics; categorized errors
- **Modular Design**: Code is reusable and testable
- **Documentation**: README, architecture, and report ready for stakeholders
- **Production Mindset**: Clean repo, reproducible environment, error handling

## Optional Deep Dives (if asked)

1. **"Why YOLOv8?"** - Fast, accurate, good transfer learning from COCO
2. **"What about tiny objects?"** - Added discussion of multi-scale detection, model architecture trade-offs
3. **"How do you handle imbalanced data?"** - Used YOLO's built-in class weighting
4. **"Can this run on edge devices?"** - YOLOv8n variant (3.2M params) for smaller devices
5. **"What's next?"** - Ensemble models, tracking across video frames, deployment to edge hardware
