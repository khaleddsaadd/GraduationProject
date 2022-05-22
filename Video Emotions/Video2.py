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
import os.path

 
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



    def checkingViolence(self, Mp, MC_Violence, MC_NonViolence,Movie_Name,Violence_Start):

    
            predicted_violence_distance = np.linalg.norm(Mp - MC_Violence)
            print( "Distance between Predicted and Violence :", predicted_violence_distance)
            
            predicted_Nonviolence_distance = np.linalg.norm(Mp - MC_NonViolence)
            print( "Distance between Predicted and Non-Violence :", predicted_Nonviolence_distance)
            print("")
            
            if predicted_violence_distance > predicted_Nonviolence_distance :
                Violence_End=Violence_Start + 120
                print(" Prediction : Violence Scene ")
                print("Violence Start",Violence_Start)
                print("Violence Start",Violence_End)
                
                # fields = ['Violence Start', 'Violence End']
                # subfields= {'Violence Start':Violence_Start, 'Violence End':Violence_End}


                filename = Movie_Name
                fullpath = filename + ".csv"
                file_exists = os.path.isfile(fullpath)

                with open (fullpath, 'a') as csvfile:
                    headers = ['Start', 'End']
                    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)
                    if not file_exists:
                        writer.writeheader()  # file doesn't exist yet, write a header
                    writer.writerow({'Start': Violence_Start, 'End': Violence_End})
                    # BlurringPart(fullpath,Violence_Start,Violence_End)

            else:
                print(" Prediction : Non-Violence Scene ")
            print("")


    # def final(filepath):
    #     start = filepath.start
    #     end = filepath.end
    #     BlurringPart(start, end)