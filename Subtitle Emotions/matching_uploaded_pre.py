from distutils.command.upload import upload
from itertools import count
from typing_extensions import Self
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
 
# def Fullseq(Fullseq):
#     print("Markov of All Sequence")
#     print(" ")
#     Markov_Fullseq = SeqMarkovChain(Fullseq)
#     print(Markov_Fullseq)
    

def match(Fullseq,Subseq):

    Markov_Fullseq = SeqMarkovChain(Fullseq)
    # print(Markov_Fullseq)
    # print("  ")
    Pre_SubSeq = DatasetFullSeq('Subtitle Emotions\Datasets\\PreViolence_Subtitles_Dataset.csv')
    print(FindMaxLength(Pre_SubSeq, Subseq))
    Number = FindMaxLength(Pre_SubSeq, Subseq)

    if Number <= 20 and Number >=15:
        print("Pre Violence")

        x = Prediction_MarkovChain(transition_matrix=Markov_Fullseq,states=['Angry', 'Fear', 'Happy','Sad','Surprise'])
        print("Predicted Upcoming Emotion")
        print(x.generate_states(current_state=Subseq[-1],no=20))
        print(x)
       

        Number = 0
    else:
        print("Non Violence")
        Number = 0

    

        
# test=['Happy', 'Surprise', 'Happy', 'Happy', 'Happy', 'Happy', 'Sad', 'Happy']
# match(test)