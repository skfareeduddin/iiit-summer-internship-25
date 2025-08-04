# Task 3: Training YOLOv8 on African Wildlife Dataset

## Objective
Fine-tune the YOLOv8 object detection model on the African Wildlife dataset and evaluate its performance using key metrics and inference results.

## Tools and Libraries Used
- Python  
- Ultralytics YOLOv8  
- NVIDIA GPU (optional but recommended for faster training)

## Workflow Summary

1. **Model Initialization**  
   Load the YOLOv8n base model from the Ultralytics hub.

2. **Training**  
   - Dataset: `african-wildlife.yaml` (4-class object detection dataset).
   - Parameters: 20 epochs, image size 640, batch size 8.
   - Training results (metrics, graphs, confusion matrix, etc.) are automatically stored in `runs/detect/train/`.

3. **Inference**  
   - Use the trained model weights (`best.pt`) to perform inference on a sample wildlife image.
   - Predicts and visualizes detected objects in the image.

## Key Outputs
- Training logs and metrics (precision, recall, mAP)
- Confusion matrix and other visual evaluation plots
- Inference output image with predicted bounding boxes

## Note
Ensure the dataset YAML file and corresponding image/label directories are correctly structured and accessible before training.
