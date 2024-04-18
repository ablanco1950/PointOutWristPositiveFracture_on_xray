# -*- coding: utf-8 -*-
# https://www.kaggle.com/datasets/pkdarabi/bone-fracture-detection-computer-vision-project/code
# https://learnopencv.com/ultralytics-yolov8/#How-to-Use-YOLOv8?
from ultralytics import YOLO
# https://pub.towardsai.net/understanding-hyper-parameter-tuning-of-yolos-82aec5f6e7b3
#model = YOLO("yolov5s.pt")
model = YOLO("yolov8s.pt")
#model=YOLO("yolov9c.pt")
#model=YOLO("best - 2epoch.pt")
#https://docs.ultralytics.com/es/guides/hyperparameter-tuning/#what-are-hyperparameters
model.train(data="FractureWristPositive.yaml", epochs=10,batch=64)  # train the model
model.val()  # evaluate model performance on the validation set
