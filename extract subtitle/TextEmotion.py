import os
import re
import pysrt
import text2emotion as te

folderpath = r"Sub" # make sure to put the 'r' in front
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
    #print(S)
    for Emotion in S:
        max_key=max(te.get_emotion(Emotion),key=te.get_emotion(Emotion).get)
        emotions.append(max_key)
    print(emotions)
    S*= 0
    emotions*=0
    print("---------------------------------------------------------------------------")
