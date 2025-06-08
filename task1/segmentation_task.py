!pip install --upgrade pip
!pip install ultralytics

from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")

results = model("https://ultralytics.com/images/bus.jpg", save=True)
results[0].show
