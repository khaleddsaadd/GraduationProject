import pandas as pd
from SeqMarkovChain import*
import re
import nltk
import numpy as np
from collections import Counter

def func(csvName):
  df = pd.read_csv(csvName)
  df.Emotions =  df.Emotions.apply(lambda x: x.replace('[','').replace(']','')) 
  df.Emotions =  df.Emotions.apply(lambda x: x.replace('"','').replace('"','')) 
  df.Emotions =  df.Emotions.apply(lambda x: x.replace(''','').replace(''','')) 

#convert the string columns to int
  df.Emotions=df.Emotions

  x= ""
  for index,row in df.iterrows():
      x = x + df.Emotions[index]
      x = x + " "
  x = x.replace(',','')
  x = x.replace("'", "")
  #print (x)
  arr = nltk.word_tokenize(x)

  #print(arr)
  a= Counter()
  b = 0
  n = 10
  f=[]  
  for x in arr :
    b+=1
    a [x]+=1
  
    if b%n == 0:
    #print (a)
      max_key = max(a, key=a.get)
      #print(max_key)
      f.append(max_key)
      a= Counter()

  #print(f)   
  SeqMarkovChain(f)


# print("Violence Dataset Markov Chain ")
# func('Video Emotions\ViolenceVi.csv')

print("Non Violence Dataset Markov Chain ")
func('Video Emotions\on-violence.csv')

