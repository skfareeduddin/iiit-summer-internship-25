# Task 5: Diabetic Foot Ulcer Detection Using YOLOv8

## Objective
Train a YOLOv8 model to detect Diabetic Foot Ulcers (DFU) using a custom-annotated dataset.

## Tools and Libraries Used
- Python  
- PyTorch  
- Ultralytics YOLOv8  
- CUDA-enabled GPU (optional)

## Workflow Summary

1. **GPU Detection**  
   - Detects and displays available GPUs along with their memory stats.
   - Falls back to CPU if no GPU is available.

2. **Dataset Configuration**  
   - Dataset structured in YOLO format and defined via `data.yaml`.
   - Dataset is stored under the `dfu_dataset` directory.

3. **Model Training**  
   - Model: `yolov8n.pt`
   - Parameters: 50 epochs, image size 512, batch size 4.
   - Training results and weights are saved under the project `dfu_ulcer_detector`.

## Key Outputs
- Trained YOLOv8 model optimized for DFU detection.
- Training logs and performance metrics including mAP, precision, and recall.
- Weights and artifacts stored under `runs/detect/dfu_ulcer_detector`.

## Note
The DFU dataset used was sourced from Kaggle and annotated manually. Ensure that the `data.yaml` file and folder structure comply with YOLOv8 training requirements.
