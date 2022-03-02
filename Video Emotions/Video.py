from msilib import sequence
import pandas as pd
from SeqMarkovChain import*
import re
import nltk
import numpy as np
from collections import Counter
import numpy as np
import csv
from csv import DictWriter
class Video(object):
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
            arr.append('Neutral')
            arr.append('Surprise')
            arr.append('Angry')
            arr.append('Happy')
            arr.append('Neutral')
            seq=arr[-500:]
            #mc da markov chain l kol film w el variable da byefda taht 3shan yetmeli tany kol mara b kol film
            mc = SeqMarkovChain(arr)
            print("Predicted Sequence for",df.Movie_Name[index])
            #predicted da bandah fe function prediction w bageb 400 sequence predicted based 3al ablo
            # w byedfda brdo m3 kol loop
            predicted=self.predictNext(current_state=seq[-1],transition_matrix=mc,
                                states=['Angry', 'Happy', 'Neutral','Sad','Surprise'], no=400)
            print(predicted)
            print("--------------------------------")
            x=x*0
            arr=arr*0
            seq=seq*0
            mc = mc*0
            predicted = predicted*0
    def next_state(self, current_state):
        return np.random.choice(
         self.states, 
         p=self.transition_matrix[self.index_dict[current_state], :]
        )
    def predictNext(self,current_state,transition_matrix, states, no=10):
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
Vv = Video(csvname='Video Emotions\Datasets\\final_previolence_movies.csv')
Vv.Start()