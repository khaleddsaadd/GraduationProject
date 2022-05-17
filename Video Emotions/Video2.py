from msilib import sequence
import pandas as pd
from scipy.fft import next_fast_len
from SeqMarkovChain import*
import re
import nltk
import numpy as np
from collections import Counter
import numpy as np
import csv
import Sub_MarkovChain as MCF
from csv import DictWriter
from scipy.spatial import distance
from csv import writer
import os
from sklearn.metrics import confusion_matrix
from sklearn import metrics


 
class Prediction_MarkovChain(object):


    def __init__(self, transition_matrix, states):
        self.transition_matrix = np.atleast_2d(transition_matrix)
        self.states = states
        self.index_dict = {self.states[index]: index for index in 
                           range(len(self.states))}
        self.state_dict = {index: self.states[index] for index in
                           range(len(self.states))}
 
    def next_state(self, current_state):
        return np.random.choice(
         self.states, 
         p=self.transition_matrix[self.index_dict[current_state], :]
        )
 
    def generate_states(self, current_state, no=20):
        future_states = []
        for i in range(no):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state
        return future_states



    def checkingViolence(self, Mp, MC_Violence, MC_NonViolence):

    
            predicted_violence_distance = np.linalg.norm(Mp - MC_Violence)
            print( "Distance between Predicted and Violence :", predicted_violence_distance)
            
            predicted_Nonviolence_distance = np.linalg.norm(Mp - MC_NonViolence)
            print( "Distance between Predicted and Non-Violence :", predicted_Nonviolence_distance)
            print("")
            
            if predicted_violence_distance > predicted_Nonviolence_distance :
                print(" Prediction : Violence Scene ")

            else:
                print(" Prediction : Non-Violence Scene ")

            print("")

