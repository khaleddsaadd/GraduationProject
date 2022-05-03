import pandas as pd
from SeqMarkovChain import*
import re
import nltk
import numpy as np

def MarkovModel(csvName):
    df = pd.read_csv(csvName)
    df['Emotions'] =  df['Emotions'].apply(lambda x: x.replace('[','').replace(']','')) 
    df['Emotions'] =  df['Emotions'].apply(lambda x: x.replace('"','').replace('"','')) 
    df['Emotions'] =  df['Emotions'].apply(lambda x: x.replace(''','').replace(''','')) 

    #convert the string columns to int
    df['Emotions'] = df['Emotions']
    x= ""
    for index,row in df.iterrows():
        x = x + df.Emotions[index]
        x = x + " "
    x = x.replace(',','')
    x = x.replace("'", "")
    # print (x)
    arr = nltk.word_tokenize(x)

    # print(arr)
    return SeqMarkovChain(arr)

print("Violence Subtitles Dataset")
print(MarkovModel('Subtitle Emotions\Datasets\\PreViolence_Subtitles_Dataset.csv'))

# print("Post-Violence Subtitles Dataset")
# print(func('Subtitle Emotions\Datasets\PostViolence_Subtitles_Dataset.csv'))

print("Non Violence Subtitles Dataset")
print(MarkovModel('Subtitle Emotions\Datasets\\NonViolence_Subtitles_Dataset.csv'))