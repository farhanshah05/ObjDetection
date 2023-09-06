from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8n.pt')
results = model("Chapter 5 - Running YOLO/Images/1.png", show = True)
cv2.waitKey(0)