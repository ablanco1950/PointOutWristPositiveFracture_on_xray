# PointOutWristPositiveFracture_on_xray

Indicate the location of wrist fractures in x-rays through training with yolo v8 of roboflow images downloaded from https://www.kaggle.com/datasets/pkdarabi/bone-fracture-detection-computer-vision-project/code

From the archive with the input files, once decompressed, the train, valid and test folders are extracted, placing them in the folder where the project is going to be executed.

A new arrangement of folders is created containing only those corresponding to Wrist Positive, successively executing

CreateTrainFractureWristPositiveYolov9.py
CreateValidFractureWristPositiveYolov9.py
CreateTestFractureWristPositiveYolov9.py

It is tested with the 6 test images

EvaluateTESTFractureWristPositiveYolov8.py

The x-rays appear on the screen, marked with a blue box, the predicted location with its confidence, and in green, the one that appears on the labels.

the attached model:

best_wrist_fracture_64Batch_10epoch.pt

has been obtained through training with:

TrainFractureWristPositiveYolov8.py

(The FractureWristPositive.yaml file contains the absolute addresses of the train and valid files, they should be changed to the absolute addresses where they are found in the project)

The log of he training is attached: LOG-TrainFractureWristPositiv_batch64_10epochs.txt

also others models with similar resultas are attached

best_wrist_fracture_128batch_10epoch.pt ( log LOG-TrainFractureWristPositiv_batch128_10epochs.txt)

and

best model - WristFracture - 2epoch – Stripped.pt

To test any set of images:

TESTFractureWristPositiveYolov8.py 

which comes prepared to test some images downloaded from https://www.kaggle.com/datasets/vuppalaadithyasairam/bone-fracture-detection-using-xrays that appear in the attached TEST1FractureWristPositive.zip compressed folder.
Changing the assignment to file on line 12, you can try any image folder

Comparing with the best model I Know: https://universe.roboflow.com/veda/bone-fracture-detection-daoon 
that only recognize and point out a wrist fracture in one image in six in testFractureWristPositive/images,  with the program EvaluateTESTFractureWristPositiveYolov8.py ( model best_wrist_fracture_64Batch_10epoch.pt )points out correctly four images and in two detects fracture but no in the same place that the label.

With the program TESTFractureWristPositiveYolov8.py , the seven wrist fractures of images in TEST1FractureWristPositive are pointed out, 
https://universe.roboflow.com/veda/bone-fracture-detection-daoon don´t recognizes any wrist fractures in images in that folder.

References:

https://universe.roboflow.com/veda/bone-fracture-detection-daoon/model/3

@misc{
                             bone-fracture-detection-daoon_dataset,
                             title = { bone fracture detection Dataset },
                             type = { Open Source Dataset },
                             author = { veda },
                             howpublished = { \url{ https://universe.roboflow.com/veda/bone-fracture-detection-daoon } },
                             url = { https://universe.roboflow.com/veda/bone-fracture-detection-daoon },
                             journal = { Roboflow Universe },
                             publisher = { Roboflow },
                             year = { 2023 },
                             month = { aug },
                             note = { visited on 2024-03-27 },
                             }

https://www.kaggle.com/code/jasonroggy/yolov8/input

https://www.kaggle.com/datasets/pkdarabi/bone-fracture-detection-computer-vision-project/code

https://github.com/ultralytics/ultralytics/issues/3629
with small dataset is not possible change optimizer neither lr parameter

https://github.com/ultralytics/yolov5/issues/6417

https://www.kaggle.com/datasets/vuppalaadithyasairam/bone-fracture-detection-using-xrays

https://github.com/ultralytics/ultralytics/issues/2721

https://docs.ultralytics.com/es/guides/hyperparameter-tuning/#what-are-hyperparameters

https://github.com/ultralytics/ultralytics/issues/2849






