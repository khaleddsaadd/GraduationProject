import os
import re
import pysrt
import text2emotion as te
from collections import Counter
import csv
from csv import DictWriter
from SeqMarkovChain import*
import nltk
print("Test")

nltk.download('omw-1.4')

folderpath = r"Subtitles_Final_Dataset/Violence Subtitles" # make sure to put the 'r' in front
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
all_files = []
S=[]
emotions=[]
i=0
for path in filepaths:
    print(path)
    subs = pysrt.open(path)

    for sub in subs:
        S.append(sub.text)
    for Emotion in S:
        max_key=max(te.get_emotion(Emotion),key=te.get_emotion(Emotion).get)
        emotions.append(max_key)
    print("Original Sequence ",emotions)
    a= Counter()
    b = 0
    n = 5
    f=[]
    for x in emotions :
      b+=1
      a [x]+=1
      
      if b%n == 0:
        max_key1 = max(a, key=a.get)
        f.append(max_key1)
        a= Counter()
    # print("\n*************************************************************************************************")
    # print("Minimized Sequence ",f) 

    fieldnames = ['Movie_Name','Emotions']
    op={'Movie_Name':path,'Emotions':emotions }

    with open(r'Subtitle Emotions\Datasets\Violence_Subtitles_Dataset.csv','a') as csv_file:
        dictwriter_object = DictWriter(csv_file, fieldnames=fieldnames)
        dictwriter_object.writerow(op)
        csv_file.close()

    S*= 0
    emotions*=0
    f*=0
    print("---------------------------------------------------------------------------")
