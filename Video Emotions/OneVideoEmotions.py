from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import math   
import matplotlib.pyplot as plt    
import pandas as pd
from keras.utils import np_utils
from skimage.transform import resize   
from itertools import islice
from collections import Counter
from SeqMarkovChain import*
from Video2 import*
import Markov_Chain as MCF

def FramesEmotions(Movie_Name,Start,End):
    face_classifier=cv2.CascadeClassifier('Video Emotions/Models/haarcascade_frontalface_default.xml')
    classifier = load_model('Video Emotions/Models/EmotionDetectionModel.h5')
    class_labels=['Angry','Happy','Neutral','Sad','Surprise']
    count = 0
    cap = cv2.VideoCapture(Movie_Name)
    success = True
    img=0
    x=0
    count = 0
    cap = cv2.VideoCapture(Movie_Name)
    success = True
    img=0
    emo=[]
    while success:
        success,image = cap.read()
        if count%30 == 0 :
             img = img+1
             if img in range(Start,End):
                #cv2.imwrite('frame%d.jpg'%img,image)
                gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)
                for (x,y,w,h) in faces:
                        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                        roi_gray=gray[y:y+h,x:x+w]
                        roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

                        if np.sum([roi_gray])!=0:
                            roi=roi_gray.astype('float')/255.0
                            roi=img_to_array(roi)
                            roi=np.expand_dims(roi,axis=0)

                            preds=classifier.predict(roi)[0]
                            label=class_labels[preds.argmax()]
                            label_position=(x,y)
                            print(label)
                            emo.append(label)
                            # Array w n-append el label feha 
                            # Call PredictNext Function 

        count+=1

    print(emo)

    emo.append('Surprise')
    emo.append('Angry')
    emo.append('Happy')
    emo.append('Neutral')
    emo.append('Sad')
    emo.append('Surprise')
    emo.append('Angry')
    emo.append('Happy')
    emo.append('Neutral')
    emo.append('Sad')

    Pre_MC=SeqMarkovChain(emo)

    x = Prediction_MarkovChain(transition_matrix=Pre_MC,states=['Angry', 'Happy', 'Neutral','Sad','Surprise'])
    VP_Emotions = x.generate_states(current_state=emo[-1],no=120)
    print("Predicted emotions from video ",VP_Emotions)
    MC_Violence = MCF.func('Video Emotions\Datasets\\final_violence_movies.csv')
    MC_NonViolence = MCF.func('Video Emotions\Datasets\\me_final_nonviolence_movies.csv')
    MP_Emotions=SeqMarkovChain(VP_Emotions)
    x.checkingViolence(MP_Emotions,MC_Violence,MC_NonViolence,Movie_Name,End)
    