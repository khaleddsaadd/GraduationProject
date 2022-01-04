import time
import os
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import math   # for mathematical operations
import matplotlib.pyplot as plt    # for plotting the images
import pandas as pd
from keras.utils import np_utils
from skimage.transform import resize   # for resizing images
from itertools import islice
from collections import Counter
from SeqMarkovChain import*
import csv
from csv import DictWriter

face_classifier=cv2.CascadeClassifier('Video Emotions/haarcascade_frontalface_default.xml')
classifier = load_model('Video Emotions/EmotionDetectionModel.h5')
# face_cascade = cv.CascadeClassifier()

class_labels=['Angry','Happy','Neutral','Sad','Surprise']

#folderpath = r"Violence Dataset" # make sure to put the 'r' in front
folderpath = r"Non-Violence Dataset"
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
all_files = []
Emotions = []

for path in filepaths:
    print(path)
    cap= cv2.VideoCapture(path)
    fps= int(cap.get(cv2.CAP_PROP_FPS))

    if cap.isOpened() == False:
        print("Error File Not Found")

    while cap.isOpened():
        frameId = cap.get(1) #current frame number
        ret,frame= cap.read()
        if ret == True:
            time.sleep(1/fps)
            labels = []
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.1,9)
            for(x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray=gray[y:y+h,x:x+w]
                roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
                if np.sum([roi_gray])!=0:
                    roi=roi_gray.astype('float')/255.0
                    roi=img_to_array(roi)
                    roi=np.expand_dims(roi,axis=0)
                    preds=classifier.predict(roi)[0]
                    label=class_labels[preds.argmax()]
                    label_position=(x,y)
                    Emotions.append(label)
                    #print(label)
                    cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
                else:
                    cv2.putText(frame,'No Face Found',(20,20),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
                
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    print(Emotions)
    fieldnames = ['Movie_Name','Emotions']
    op={'Movie_Name':path,'Emotions':Emotions }
    with open(r'Video Emotions\on-violence.csv','a') as csv_file:
    # with open(r'ViolenceVi.csv','a') as csv_file:
        dictwriter_object = DictWriter(csv_file, fieldnames=fieldnames)
        dictwriter_object.writerow(op)
        csv_file.close()
    print("*****************")
    Emotions*=0
print("end")
