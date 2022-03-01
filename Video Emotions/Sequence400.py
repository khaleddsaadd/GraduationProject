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
      arr2=arr[-400:]
      print(len(arr2))
      print(arr2)
      x=x*0
      arr=arr*0
      arr2=arr2*0

##func ("C:\xampp\htdocs\GraduationProject\Video Emotions\Datasets\final_previolence_movies.csv")
func('Video Emotions\Datasets\\final_previolence_movies.csv')

 