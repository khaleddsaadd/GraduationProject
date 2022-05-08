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

def DatasetFullSeq(csvName):
    df = pd.read_csv(csvName)
    df['Emotions'] =  df['Emotions'].apply(lambda x: x.replace('[','').replace(']','')) 
    df['Emotions'] =  df['Emotions'].apply(lambda x: x.replace('"','').replace('"','')) 
    df['Emotions'] =  df['Emotions'].apply(lambda x: x.replace(''','').replace(''','')) 

    #convert the string columns to int
    df['Emotions'] = df['Emotions']
    # print(df['Emotions'.count])
    # ehh = []
    # num = 0
    # count=0
    # for i in range (len(df.Emotions)):
    #     count = count + 1
    #     # print(df.Emotions[i])
    #     # print(" ")
    #     khaled = df.Emotions[i]
    #     khaled = khaled.replace(',','')
    #     khaled = khaled.replace("'", "")
    #     zaha2 = nltk.word_tokenize(khaled)
    #     print(len(zaha2))
    #     num = num + len(zaha2)
    #     # print(num)
    #     print("")
    # # print(num/count)

    x= ""
    for index,row in df.iterrows():
        x = x + df.Emotions[index]
        x = x + " "
    x = x.replace(',','')
    x = x.replace("'", "")
    arr = nltk.word_tokenize(x)
    return arr
    

# print("Violence Subtitles Dataset")
# print(MarkovModel('Subtitle Emotions\Datasets\\PreViolence_Subtitles_Dataset.csv'))

# # print("Post-Violence Subtitles Dataset")
# # print(func('Subtitle Emotions\Datasets\PostViolence_Subtitles_Dataset.csv'))

# print("Non Violence Subtitles Dataset")
# print(MarkovModel('Subtitle Emotions\Datasets\\NonViolence_Subtitles_Dataset.csv'))

# print(DatasetFullSeq('Subtitle Emotions\Datasets\\PreViolence_Subtitles_Dataset.csv'))