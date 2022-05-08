from distutils.command.upload import upload
from itertools import count
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
 
def match(Fullseq,Subseq,SubTime):

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
        #Function Reem w Tamer ()
        print("----------------------------------")
        Number = 0
    else:
        print("Non Violence")
        Number = 0

    

        
# test=['Happy', 'Surprise', 'Happy', 'Happy', 'Happy', 'Happy', 'Sad', 'Happy']
# match(test)