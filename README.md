# Muscle Force Calculator
The purpose of this project is to display a real-time augmented reality overlay of the human body, with the focus on calculating the forces acting on the bicep muscles through the use of a single camera.

This project uses the Python plugin MediaPipe for real-time pose detection, from which 3-Dimensional coordinates can be extrapolated. With this, the angles of a user's joints can be found, which is used to find the force placed upon the biceps.

The following packages are needed in order to run this in Python:
- numpy
- matplotlib
- mediapipe
- opencv-python
- tkinter
- pillow

To run the program, clone or download this repo, navigate into the project folder, install the listed packages, and run the program via `start.py`

**Note: Python Version 3.10.9 is the latest version that is supported by all the packages used, so I recommend you use that.
