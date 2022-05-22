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

def FramesEmotions(Movie_Name,Start_in_sec,End_in_sec):
    face_classifier=cv2.CascadeClassifier('Video Emotions/Models/haarcascade_frontalface_default.xml')
    classifier = load_model('Video Emotions/Models/EmotionDetectionModel.h5')
    class_labels=['Angry','Happy','Neutral','Sad','Surprise']
    start_time_ms = Start_in_sec * 1000
    stop_time_ms = End_in_sec * 1000
    vidcap = cv2.VideoCapture(Movie_Name)
    count = 0
    success = True
    emo=[]

    vidcap.set(cv2.CAP_PROP_POS_MSEC,start_time_ms)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    while success and vidcap.get(cv2.CAP_PROP_POS_MSEC) <= stop_time_ms:
        success, image = vidcap.read()
        # print('Read a new frame: ', success)
        if count%fps == 0:
            # cv2.imwrite("frame%d.jpg" % count, image)  
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
        count += 1
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
    x.checkingViolence(MP_Emotions,MC_Violence,MC_NonViolence,Movie_Name,End_in_sec)
    