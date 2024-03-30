# -*- coding: utf-8 -*-
"""
Created on Mar 2024

@author: Alfonso Blanco
"""
#######################################################################
# PARAMETERS
######################################################################
dir=""
# from https://www.kaggle.com/datasets/vuppalaadithyasairam/bone-fracture-detection-using-xrays
dirname= "TEST1FractureWristPositive"

dirnameYolo="best - WristFracture - 2epoch - Stripped.pt"


import cv2
import time
Ini=time.time()



# https://docs.ultralytics.com/python/
from ultralytics import YOLO
model = YOLO(dirnameYolo)

class_list = model.model.names
print(class_list)

import numpy as np


import os
import re

import imutils

import numpy


########################################################################
def loadimages(dirname):
 #########################################################################
 # adapted from:
 #  https://www.aprendemachinelearning.com/clasificacion-de-imagenes-en-python/
 # by Alfonso Blanco García
 ########################################################################  
     imgpath = dirname + "\\"
     
     images = []
     TabFileName=[]
   
    
     print("Reading imagenes from ",imgpath)
     NumImage=-2
     
     Cont=0
     for root, dirnames, filenames in os.walk(imgpath):
        
         NumImage=NumImage+1
         
         for filename in filenames:
             
             if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                 
                 
                 filepath = os.path.join(root, filename)
                
                 
                 image = cv2.imread(filepath)
                 gray=image
                 #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                 gray=cv2.resize(gray,(640,640))                           
                 images.append(gray)
                 TabFileName.append(filename)
                 
                 Cont+=1
     
     return images, TabFileName

# ttps://medium.chom/@chanon.krittapholchai/build-object-detection-gui-with-yolov8-and-pysimplegui-76d5f5464d6c
def DetectBoneFractureWithYolov8 (img):
  
   TabcropBoneFracture=[]
   
   y=[]
   yMax=[]
   x=[]
   xMax=[]
   Tabclass_name=[]
   results = model.predict(img)
   for i in range(len(results)):
       # may be several plates in a frame
       result=results[i]
       
       xyxy= result.boxes.xyxy.numpy()
       confidence= result.boxes.conf.numpy()

       print(confidence)
       
       if len(confidence) == 0: continue
       if float(confidence[0]) < 0.4: continue
       class_id= result.boxes.cls.numpy().astype(int)
       print(class_id)
       out_image = img.copy()
       for j in range(len(class_id)):
           con=confidence[j]
           label=class_list[class_id[j]] + " " + str(con)
           box=xyxy[j]
           
           cropBoneFracture=out_image[int(box[1]):int(box[3]),int(box[0]):int(box[2])]
           
           TabcropBoneFracture.append(cropBoneFracture)
           y.append(int(box[1]))
           yMax.append(int(box[3]))
           x.append(int(box[0]))
           xMax.append(int(box[2]))
           #Tabclass_name.append(class_name)
           print(label)
           Tabclass_name.append(label)
            
      
   return TabcropBoneFracture, y,yMax,x,xMax, Tabclass_name


###########################################################
# MAIN
##########################################################


imagesComplete, TabFileName=loadimages(dirname)

print("Number of images : " + str(len(imagesComplete)))

ContError=0
ContHit=0
ContNoDetected=0

for i in range (len(imagesComplete)):
 
           
            gray=imagesComplete[i]
            #print(gray.shape)

            imgTrue=imagesComplete[i]
            
            TabImgSelect, y, yMax, x, xMax, Tabclass_name =DetectBoneFractureWithYolov8(gray)
            
            if TabImgSelect==[]:
                print(TabFileName[i] + " NON DETECTED")
                ContNoDetected=ContNoDetected+1 
                continue
            else:
                #ContDetected=ContDetected+1
                print(TabFileName[i] + " DETECTED ")
                
                
            for z in range(len(TabImgSelect)):
                #if TabImgSelect[z] == []: continue
                gray1=TabImgSelect[z]
                #cv2.waitKey(0)
                start_point=(x[z],y[z]) 
                end_point=(xMax[z], yMax[z])
                color=(255,0,0)
                # Using cv2.rectangle() method
                # Draw a rectangle with blue line borders of thickness of 5 px
                img = cv2.rectangle(gray, start_point, end_point,(255,0,0), 2)
                # Put text
                text_location = (x[z], y[z])
                text_color = (255,255,255)
              
                cv2.putText(img, str(Tabclass_name[z]) ,text_location
                        , cv2.FONT_HERSHEY_SIMPLEX , 1
                        , text_color, 2 ,cv2.LINE_AA)
                cv2.putText(gray1, str(Tabclass_name[z]) ,text_location
                        , cv2.FONT_HERSHEY_SIMPLEX , 1
                        , text_color, 2 ,cv2.LINE_AA)
                        
                #cv2.imshow('Bone Fracture', gray1)
                #cv2.waitKey(0)
                break
            #      
            #show_image=cv2.resize(img,(1000,700))
            #cv2.imshow('Frame', show_image)
            cv2.imshow('Frame', img)
            cv2.waitKey(0)
           
             
              
print("")           
print("NO detected=" + str(ContNoDetected))
print("")      
print( " Time in seconds "+ str(time.time()-Ini))
