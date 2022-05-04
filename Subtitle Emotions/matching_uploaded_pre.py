from distutils.command.upload import upload
from itertools import count
from numpy import mat
from SeqMarkovChain import*
from Sub_MarkovChain import*
from distutils.command.upload import upload
from itertools import count
from numpy import mat
from SeqMarkovChain import*
from Sub_MarkovChain import*

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
 
 
def match(uploaded):
    # print(uploaded)
    Pre_SubSeq = DatasetFullSeq('Subtitle Emotions\Datasets\\PreViolence_Subtitles_Dataset.csv')
    print(FindMaxLength(Pre_SubSeq, uploaded))
    Number = FindMaxLength(Pre_SubSeq, uploaded)
    if Number <= 20 and Number >=15:
        print("Pre Violence")
        Number = 0
    else:
        print("Non Violence")
        Number = 0

        
# test=['Happy', 'Surprise', 'Happy', 'Happy', 'Happy', 'Happy', 'Sad', 'Happy']
# match(test)