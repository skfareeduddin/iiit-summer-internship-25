from ultralytics import YOLO
import os

model = YOLO('yolov8n-seg.pt')
os.makedirs('ouput_images', exist_ok=True)

image_paths = [
    'input_images/image1.jpg', 
    'input_images/image2.jpg', 
    'input_images/image3.jpg', 
    'input_images/image4.jpg'
    ]

for img_path in image_paths:
    results = model(img_path)
    
    results[0].save()

print("Segmentation completed!")
