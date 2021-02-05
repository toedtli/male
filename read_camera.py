#!/usr/bin/python3
#https://maker.pro/nvidia-jetson/tutorial/streaming-real-time-video-from-rpi-camera-to-browser-on-jetson-nano-with-flask
import cv2
import matplotlib.pyplot as plt
GSTREAMER_PIPELINE = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink wait-on-eos=false max-buffers=1 drop=True'
video_capture = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)
return_key, frame = video_capture.read()
video_capture.release()
frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imsave('cameratest.png',frame_rgb )
