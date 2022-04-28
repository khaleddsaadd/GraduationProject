
from msilib import sequence
import pandas as pd
from SeqMarkovChain import*
import re
import nltk
import numpy as np
from collections import Counter
import numpy as np
import csv
import Markov_Chain as MCF
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
            arr.append('Neutral')
            arr.append('Surprise')
            arr.append('Angry')
            arr.append('Happy')
            arr.append('Neutral')

            mc = SeqMarkovChain(arr)

        

    