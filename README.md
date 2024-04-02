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

the attached model:

best model - WristFracture - 2epoch – Stripped.pt

has been obtained through training with:

TrainFractureWristPositiveYolov8.py
(The FractureWristPositive.yaml file contains the absolute addresses of the train and valid files, they should be changed to the absolute addresses where they are found in the project)

And by the procedure, not at all academic, of testing the best.pt file that is produced in each epoch and saving the one that gives the best results, despite what yolo indicates (The logs with excellent map5O values are attached as txt files, which do not correspond to the results when treating unseen data). And I  have found problems changing the hyperparameters of yolo. Transferring records from the train to the valid one so that a 2/3 ratio is met, also does not achieve improvements

The best best.pt, in practice (with unseen data), in PointOutWristPositiveFracture_on_xray\runs\detect\trainnn\weights is saved and its size is reduced using the OptimizerStripped.py program so that it can be uploaded to github.

To test any set of images:

TESTFractureWristPositiveYolov8.py 

which comes prepared to test some images downloaded from https://www.kaggle.com/datasets/vuppalaadithyasairam/bone-fracture-detection-using-xrays that appear in the attached TEST1FractureWristPositive.zip compressed folder.
Changing the assignment to file on line 12, you can try any image folder

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

https://www.kaggle.com/datasets/vuppalaadithyasairam/bone-fracture-detection-using-xrays

https://github.com/ultralytics/ultralytics/issues/2721

https://docs.ultralytics.com/es/guides/hyperparameter-tuning/#what-are-hyperparameters

https://github.com/ultralytics/ultralytics/issues/2849

