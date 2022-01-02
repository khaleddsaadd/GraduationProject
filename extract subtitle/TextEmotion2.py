import pandas as pd
from SeqMarkovChain import*
import nltk
import numpy as np
dataset = pd.read_csv("Emotions Dataset.csv")

df = pd.read_csv('Emotions Dataset.csv')
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
print (x)
arr = nltk.word_tokenize(x)

print(arr)
SeqMarkovChain(arr)