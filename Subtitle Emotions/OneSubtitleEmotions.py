import os
import re
import pysrt
import text2emotion as te
from collections import Counter
import csv
from csv import DictWriter
from SeqMarkovChain import*
import nltk
# nltk.download('omw-1.4')


def OneSubtitleEmotions (subtitlefile):
    S=[]
    emotions=[]
    Start=[]
    i=0
    filepath = subtitlefile
    subs = pysrt.open(filepath)

    for sub in subs:
        S.append(sub.text)
        start = sub.start.to_time()
        Start.append(str(start))
    for Emotion in S:
        max_key=max(te.get_emotion(Emotion),key=te.get_emotion(Emotion).get)
        emotions.append(max_key)
    # print("Original Sequence ",emotions)
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
    return emotions , Start
    # print(len(emotions))
    # print(len(Start))

OneSubtitleEmotions('Subtitles\\Non Violence Subtitles\\6Underground1.txt')
# Start = []
# sub = pysrt.open("Subtitles\\Non Violence Subtitles\\6Underground1.txt")
# for i in range (len(sub)):
#     start = sub[i].start.to_time()
#     end = sub[i].end.to_time()
#     Start.append(str(start))

# print(Start)