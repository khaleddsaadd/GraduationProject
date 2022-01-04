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

count = 0
videoFile = r"Videos/Demo.mp4"
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1


face_classifier=cv2.CascadeClassifier('Video Emotions/haarcascade_frontalface_default.xml')
classifier = load_model('Video Emotions/EmotionDetectionModel.h5')

class_labels=['Angry','Happy','Neutral','Sad','Surprise']

# cap=cv2.VideoCapture(0)
#Array to store the sequence of emotions
Emotions = []

while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename ="frame%d.jpg" % count;count+=1
    labels=[]
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
   
    for (x,y,w,h) in faces:
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
    
    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
print ("Done!")
print(Emotions)
cv2.destroyAllWindows()

a= Counter()
b = 0
n = 5
f=[]
for x in Emotions :
  b+=1
  a [x]+=1
  
  if b%n == 0:
   #print (a)
   max_key = max(a, key=a.get)
  #print(max_key)
   f.append(max_key)
   a= Counter()

print(f)   

SeqMarkovChain(f)


