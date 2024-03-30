# -*- coding: utf-8 -*-
# https://www.kaggle.com/datasets/pkdarabi/bone-fracture-detection-computer-vision-project/code
# https://learnopencv.com/ultralytics-yolov8/#How-to-Use-YOLOv8?
from ultralytics import YOLO

model = YOLO("yolov8s.pt")
#model=YOLO("yolov9c.pt")
#model=YOLO("best - 2epoch.pt")
model.train(data="FractureWristPositive.yaml", epochs=10)  # train the model
model.val()  # evaluate model performance on the validation set
