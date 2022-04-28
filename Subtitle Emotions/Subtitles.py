
from msilib import sequence
import pandas as pd
from SeqMarkovChain import*
import re
import nltk
import numpy as np
from collections import Counter
import numpy as np
import csv
import Sub_MarkovChain as MCF
from csv import DictWriter
from scipy.spatial import distance
from csv import writer
import os
from sklearn.metrics import confusion_matrix
from sklearn import metrics


class Subtitles():
    def __init__(self,csvname):
        self.csvname = csvname
    def Start(self):
        df = pd.read_csv(self.csvname)
        df.Emotions =  df.Emotions.apply(lambda x: x.replace('[','').replace(']','')) 
        df.Emotions =  df.Emotions.apply(lambda x: x.replace('"','').replace('"','')) 
        df.Emotions =  df.Emotions.apply(lambda x: x.replace(''','').replace(''','')) 
        df.Emotions=df.Emotions
        x= ""
        for index,row in df.iterrows():
            x = x + df.Emotions[index]
            x = x + " "
            x = x.replace(',','')
            x = x.replace("'", "")
            arr = nltk.word_tokenize(x)
            arr.append('Surprise')
            arr.append('Angry')
            arr.append('Happy')
            arr.append('Sad')
            arr.append('Fear')
            arr.append('Surprise')
            arr.append('Angry')
            arr.append('Happy')
            arr.append('Fear')
            arr.append('Sad')

            print (arr)
        
            mc = SeqMarkovChain(arr)
            predicted=self.predictNext(current_state=arr[-1],transition_matrix=mc,
                                states=['Angry', 'Fear', 'Happy','Sad','Surprise'], no=30)
            
            predicted.append('Surprise')
            predicted.append('Angry')
            predicted.append('Happy')
            predicted.append('Sad')
            predicted.append('Surprise')
            predicted.append('Angry')
            predicted.append('Happy')
            predicted.append('Sad')

            print("")
            print("Predicted Emotions of ", df.Movie_Name[index])
            print("")
            print(predicted)
            
            Mp = SeqMarkovChain(predicted)
            print("")
            print(" Markov Chain of Predicted Emotions ")
            print("")

            print(Mp)

            print("")
            x=x*0
            arr=arr*0
            mc = mc*0
            predicted = predicted*0
            Mp = Mp*0

    def next_state(self, current_state):
        return np.random.choice(
         self.states, 
         p=self.transition_matrix[self.index_dict[current_state], :]
        )
    def predictNext(self,current_state,transition_matrix, states, no=30):
        self.transition_matrix = np.atleast_2d(transition_matrix)
        self.states = states
        self.index_dict = {self.states[index]: index for index in 
                           range(len(self.states))}
        self.state_dict = {index: self.states[index] for index in
                           range(len(self.states))}
        future_states = []
        for i in range(no):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state
        return future_states
        

Vv = Subtitles(csvname='Subtitle Emotions\Datasets\PreViolence_Subtitles_Dataset.csv')
Vv.Start()
