# -*- coding: utf-8 -*-
"""
Created on Apr 2024

@author: Alfonso Blanco
"""
#######################################################################
# PARAMETERS
######################################################################
dir=""
dirname= "test\\images\\"
dirnameLabels="test\\labels\\"
Outputdirname= "testFractureWristPositive\\images"
OutputdirnameLabels="testFractureWristPositive\\labels"
import os

import shutil
output_dir="testFractureWristPositive"

if  os.path.exists(output_dir):shutil.rmtree(output_dir)
os.mkdir(output_dir)
os.mkdir(Outputdirname)
os.mkdir(OutputdirnameLabels)


import cv2
import time
Ini=time.time()

import numpy as np

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
     dirname = dirname + "\\"
     
     images = []
     TabFileName=[]
   
    
     #print("Reading imagenes from ",dirname)
     NumImage=-2
     
     Cont=0
     for root, dirnames, filenames in os.walk(dirname):
        
         NumImage=NumImage+1
         
         for filename in filenames:
             
             if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                 
                 
                 filepath = os.path.join(root, filename)
                
                 
                 image = cv2.imread(filepath)
                                            
                 images.append(image)
                 TabFileName.append(filename)
                 
     
     return images, TabFileName
########################################################################
def loadlabels(dirnameLabels):
 #########################################################################
 # adapted from:
 #  https://www.aprendemachinelearning.com/clasificacion-de-imagenes-en-python/
 # by Alfonso Blanco García
 ########################################################################  
     dirnameLabels = dirnameLabels + "\\"
     
     Labels = []
     TabFileLabelsName=[]
     TabLineaLabel=[]
     ContLabels=0
     ContNoLabels=0
     
    
     print("Reading labels from ",dirnameLabels)
    
    
     for root, dirnames, filenames in os.walk(dirnameLabels):
        
         
         
         for filename in filenames:
              
             
                           
                 filepath = os.path.join(root, filename)
                
                 f=open(filepath,"r")

                 
                 LineaLabel=""
                 
                 for linea in f:
                      LineaLabel=linea 
                      break
                               
                 if LineaLabel=="":
                      ContLabels+=1
                 else:
                     ContNoLabels+=1

                     
                 TabLineaLabel.append(LineaLabel)
                 TabFileLabelsName.append(filename)
                 
     #print("Number of files labels : " + str(len(Labels)))

     #print("Number of files without labels : " + str(ContNoLabels))
     #print("Number of files with labels : " + str(ContLabels))            
     return  TabFileLabelsName, TabLineaLabel,ContLabels, ContNoLabels




###########################################################
# MAIN
##########################################################

TabFileLabelsName, TabLineaLabel, ContLabels, ContNoLabels= loadlabels(dirnameLabels)




imagesComplete, TabFileName=loadimages(dirname)

print("Number of images : " + str(len(imagesComplete)))

ContWristPositiv=0
ContShoulderFractured=0
for i in range (len(imagesComplete)):
 
            if TabFileLabelsName[i][:len(TabFileLabelsName[i])-4] != TabFileName[i][:len(TabFileName[i])-4]:
                 print("ERROR SEQUENCING IMAGES AND LABELS " + TabFileLabelsName[i][:len(TabFileLabelsName[i])-4] +" --" + TabFileName[i][:len(TabFileName[i])-4])
                 break


            f=open(dirnameLabels +TabFileLabelsName[i],"r")

                 
            LineaLabel=""
                 
            for linea in f:
                      #print(linea)
                      LineaLabel=linea 
                      lineadelTrain =linea.split(" ")
                      indexFracture=int(lineadelTrain[0])
                      #Label=class_list[indexFracture]  
            # no se consideran las que no vienen labeladas
            if LineaLabel == "": continue

            #lineadelTrain =TabLineaLabel[i].split(" ")
           
            #indexFracture=int(lineadelTrain[0])
            if indexFracture==6:
                  lineadelTrain[0]= 0
                  ContWristPositiv+=1
            else:
                 continue
            gray = cv2.cvtColor(imagesComplete[i], cv2.COLOR_BGR2GRAY)
            gray=cv2.resize(gray,(640,640))
            cv2.imwrite(Outputdirname+ "\\" + TabFileName[i],gray)
            with open( OutputdirnameLabels + "\\" +TabFileLabelsName[i] ,"w") as  w:
               #print(lineadelTrain)
               #print(lineadelTrain[0])
                 
               lineaWrite=""
               for j in range (len(lineadelTrain)):
                    if j > 0:
                         lineaWrite=lineaWrite+ " " + str(float(lineadelTrain[j]))
                    else:
                         lineaWrite=lineaWrite+  str(lineadelTrain[0])
                      
               #lineaWrite =' '.join(lineadelTrain)
               lineaWrite=lineaWrite + "\n"
               #print(lineaWrite)
               w.write(lineaWrite)
               w.close
  
              
print("")           

print("Number of records to test Wrist Positive = " + str(ContWristPositiv))

      
print( " Time in seconds "+ str(time.time()-Ini))
