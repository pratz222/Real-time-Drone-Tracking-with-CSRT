# Real-time Drone Tracking with CSRT

## Overview
This project implements real-time object tracking using the CSRT algorithm from the OpenCV library. It captures video input from a file (e.g., `Drone.mp4`) or webcam, allowing the user to select an object to track by drawing a bounding box around it. The tracker updates the position of the object in each frame, drawing a green rectangle around it.

## Hardware Requirements
- **Computer/Laptop**: Required for running the OpenCV code.
- **Webcam (optional)**: If you want to track objects in real-time via live camera feed.

## Software Requirements
- **OpenCV**: Make sure to install the OpenCV library for Python. You can install it using pip:
  ```bash
  pip install opencv-python
  ```

## Pin Details and Configuration
Since this project primarily involves software, there are no specific hardware pin configurations. However, if you are using a webcam, ensure that it is properly connected to your computer.

## Execution
1. **Run the Code**: Execute the script in an environment that supports OpenCV.
2. **Select Object**: When prompted, draw a bounding box around the object you wish to track.
3. **Tracking**: The program will track the object in the video feed until you press 'e' to exit.


![track](https://github.com/pratz222/Real-time-Drone-Tracking-with-CSRT/assets/53640877/6fda7c1a-a76d-4542-993e-832275e49a77)
