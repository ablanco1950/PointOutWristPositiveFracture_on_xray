# PointOutWristPositiveFracture_on_xray

Indicate the location of wrist fractures in x-rays through training with yolo v8 of roboflow images downloaded from https://www.kaggle.com/datasets/pkdarabi/bone-fracture-detection-computer-vision-project/code

From the archive with the input files, once decompressed, the train, valid and test folders are extracted, placing them in the folder where the project is going to be executed.

A new arrangement of folders is created containing only those corresponding to Wrist Positive, successively executing

CreateTrainFractureWristPositiveYolov9.py
CreateValidFractureWristPositiveYolov9.py
CreateTestFractureWristPositiveYolov9.py

It is tested with the 6 test images

EvaluateTESTFractureWristPositiveYolov8.py

The x-rays appear on the screen, marked with a blue box, the predicted location with its confidence, and in green, the one that appears on the labels (due to lack of documentation on the labels of the train file, its meaning cannot be specified, although it seems that one is a rude location and the other tighter)

the best model - WristFracture - 2epoch – Stripped.pt

has been obtained through training with:

TrainFractureWristPositiveYolov8.py
(The FractureWristPositive.yaml file contains the absolute addresses of the train and valid files, they should be changed to the absolute addresses where they are found in the project)

and by the procedure, not at all academic, of testing the best.pt file that is produced in each epoch and saving the one that gives the best results, despite what yolo indicates. The best best.pt, in practice, in PointOutWristPositiveFracture_on_xray\runs\detect\train\weights is saved and its size is reduced using the OptimizerStripped.py program so that it can be uploaded to github.

Note: the trained images have been converted to gray and formatted 640x640. The images to be tested have to be converted to this format to obtain best results

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

https://www.kaggle.com/datasets/pkdarabi/bone-fracture-detection-computer-vision-project/code

https://github.com/ultralytics/yolov5/issues/6417
