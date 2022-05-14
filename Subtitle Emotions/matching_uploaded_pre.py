from distutils.command.upload import upload
from itertools import count
from os import system
# from typing_extensions import Self
from numpy import mat
from SeqMarkovChain import*
from Sub_MarkovChain import*
from distutils.command.upload import upload
from itertools import count
from numpy import mat
from SeqMarkovChain import*
from Sub_MarkovChain import*
from Subtitles2 import*
import sys
from moviepy.editor import *
import datetime
import sys
sys.path.append('Video Emotions')
from OneVideoEmotions import FramesEmotions

def FindMaxLength(A, B):
    n = len(A)
    m = len(B)
    dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if A[i] == B[j]:
                dp[j][i] = dp[j + 1][i + 1] + 1
    maxm = 0
    for i in dp:
        for j in i:
             maxm = max(maxm, j)
    return maxm
 
def match(Fullseq,Subseq,SubTime,M_Name):
    # sys.path.append('../GUI')
    # from input import browseMovie
    Markov_Fullseq = SeqMarkovChain(Fullseq)
    print("Subsequence Emotions ")
    S= Subseq
    print(S)
    print(" ")
    print("Subsequence Times")
    T= SubTime
    print(T)
    print(" ")
    Pre_SubSeq = DatasetFullSeq('Subtitle Emotions\Datasets\\PreViolence_Subtitles_Dataset.csv')
    Number = FindMaxLength(Pre_SubSeq, Subseq)
    # print(sys.path)
    print("Number of matched emotions with Pre CSV",Number)
    print(" ")
    if Number in range(10, 30):
        print("Scene Status: Pre Violence")
        x = Prediction_MarkovChain(transition_matrix=Markov_Fullseq,states=['Angry', 'Fear', 'Happy','Sad','Surprise'])
        print(" ")
        print("Predicted Upcoming Emotion")
        print(x.generate_states(current_state=Subseq[-1],no=20))
        print(" ")
        Pre_Start = SubTime[0]
        Pre_End = SubTime[-1]
        print("Pre Scene Start Time: ",Pre_Start)
        print(" ")
        print("Pre Scene End Time: ",Pre_End)
        print(" ")
        print(type(Pre_End))
        Prevideo = SubVideo(Pre_Start,Pre_End,M_Name)
        #Function Reem w Tamer ()
        
        print("----------------------------------")
        Number = 0
        
    else:
        print("Non Violence")
        Number = 0

  
# Start_pre=[]
# End_pre=[]

def SubVideo(x,y,movie):
    date_time = datetime.datetime.strptime(x, "%H:%M:%S.%f")
    print(date_time)
    
    a_timedelta = date_time - datetime.datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()

    date_time_2 = datetime.datetime.strptime(y, "%H:%M:%S.%f")

    print(date_time_2)
    
    a_timedelta_2 = date_time_2 - datetime.datetime(1900, 1, 1)
    seconds_end = a_timedelta_2.total_seconds()
    
    print("Starrt ",seconds)
    print("endd ",seconds_end)
    
    print(movie)
    FramesEmotions(movie,int(seconds),int(seconds_end))

#    clip = VideoFileClip(movie) 
#    clip = clip.subclip(seconds, seconds_end)
#    #clip.preview()
#    return clip

   



        
# test=['Happy', 'Surprise', 'Happy', 'Happy', 'Happy', 'Happy', 'Sad', 'Happy']
# match(test)
