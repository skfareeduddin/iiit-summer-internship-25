from ultralytics import YOLO
import os

os.makedirs('input_video', exist_ok=True)
os.makedirs('frames', exist_ok=True)
os.makedirs('segmented_frames', exist_ok=True)
os.makedirs('output_video', exist_ok=True)

frames_folder = 'frames'
segmented_folder = 'segmented_frames'
output_video_path = 'output_video/output_segmented_video.mp4'

frame_files = sorted(os.listdir(frames_folder))

model = YOLO('yolov8n-seg.pt')

for frame_file in frame_files:
    frame_path = os.path.join(frames_folder, frame_file)
    results = model(frame_path)

    save_path = os.path.join(segmented_folder, frame_file)
    results[0].save(filename=save_path)
