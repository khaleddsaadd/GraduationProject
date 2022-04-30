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


class Subtitles(object):
    pred=[]
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
            predicted.append('Fear')
            predicted.append('Surprise')
            predicted.append('Angry')
            predicted.append('Happy')
            predicted.append('Sad')
            predicted.append('Fear')

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
                        
            MC_Violence = MCF.func('Subtitle Emotions\Datasets\\Violence_Subtitles_Dataset.csv')
            MC_NonViolence = MCF.func('Subtitle Emotions\Datasets\\NonViolence_Subtitles_Dataset.csv')

            check= self.checkingViolence(Mp, MC_Violence, MC_NonViolence)
            print(check)

            print("-------------------------------------------------------------------------------------------------------------------------------------------")


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

    def checkingViolence(self, Mp, MC_Violence, MC_NonViolence):

 
        predicted_violence_distance = np.linalg.norm(Mp - MC_Violence)
        print( "Distance between Predicted and Violence :", predicted_violence_distance)
        
        predicted_Nonviolence_distance = np.linalg.norm(Mp - MC_NonViolence)
        print( "Distance between Predicted and Non-Violence :", predicted_Nonviolence_distance)
        print("")
        
        if predicted_violence_distance > predicted_Nonviolence_distance :
            print(" Prediction : Violence Scene ")
            self.pred.append("V")

        else:
            print(" Prediction : Non-Violence Scene ")
            self.pred.append("N")

        print("")

        

Vv = Subtitles(csvname='Subtitle Emotions\Datasets\\PreViolence_Subtitles_Dataset.csv')
Vv.Start()

# df = pd.read_csv("C:/xampp/htdocs/GraduationProject/Video Emotions/predvsact.csv")
# df["Predection"] = ""
# df.to_csv("C:/xampp/htdocs/GraduationProject/Video Emotions/predvsact.csv", index=False)

df = pd.read_csv("Subtitle Emotions/predvsactS.csv")
df["Predection"] = Vv.pred
df.to_csv("Subtitle Emotions/predvsactS.csv", index=False)

col_list = ["Actual", "Predection"]
df = pd.read_csv("Subtitle Emotions/predvsactS.csv", usecols=col_list)

y_true = df["Actual"]
y_pred = df["Predection"]

print(confusion_matrix(y_true, y_pred))
print(metrics.confusion_matrix(y_true, y_pred))
print(metrics.classification_report(y_true, y_pred))