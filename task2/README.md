# Task 2: Image and Video Segmentation using YOLOv8

## Objective
Perform segmentation on a batch of local images and video frames using YOLOv8. This task includes both image-wise and frame-wise segmentation, saving the outputs for further processing or reconstruction.

## Tools and Libraries Used
- Python  
- Ultralytics YOLOv8  
- OS module for directory handling

## Files Description

### segment_custom_images.py
- Performs segmentation on a predefined list of local images stored in `input_images/`.
- Saves segmented outputs to `output_images/`.

### segment_video_frames.py
- Loads individual frames from the `frames/` folder.
- Applies YOLOv8 segmentation to each frame.
- Saves results to `segmented_frames/`.

## Output
- Segmented images and frames are saved locally.
- Final output video can be created using `ffmpeg` by combining the segmented frames from `segmented_frames/`.

## Note
- Place all input images and video frames in their respective folders before running the scripts.
- Use `ffmpeg` or any preferred tool for:
  - Extracting frames from a video into the `frames/` folder
  - Reconstructing segmented frames into a video inside `output_video/`
