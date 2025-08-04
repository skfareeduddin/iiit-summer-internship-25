# Task 4: Custom Object Detection with YOLOv8

## Objective
Train a YOLOv8 model on a self-created custom dataset with manually annotated images, and perform object detection on a test video.

## Tools and Libraries Used
- Python  
- PyTorch  
- Ultralytics YOLOv8  
- GPU (CUDA) for accelerated training (optional)

## Workflow Summary

1. **Device Check**  
   Check if a CUDA-compatible GPU is available to utilize for training.

2. **Model Training**  
   - Custom dataset defined in `data.yaml`.
   - Parameters: 20 epochs, image size 640, batch size 4.
   - Training outputs are stored in `runs/detect/train/`.

3. **Inference on Video**  
   - Use the best trained model (`best.pt`) to perform inference on `test_video.mp4`.
   - Output video is saved with bounding box predictions.

## Key Outputs
- Trained model weights
- Training metrics and plots (mAP, precision, recall)
- Predicted video with detected objects

## Note
The dataset used was custom-annotated using tools like Roboflow or LabelImg. Ensure your `data.yaml` and dataset folders follow YOLO format before training.
