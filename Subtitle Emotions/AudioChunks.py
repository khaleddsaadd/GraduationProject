
# filename = r'C:\Users\world\16-122828-0002.wav'

# # initialize the recognizer
# r = sr.Recognizer()
# # open the file
# with sr.AudioFile(filename) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)
    

from textblob import TextBlob
from nltk.util import pr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# importing libraries 
import moviepy.editor as mp
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

clip = mp.VideoFileClip(r"C:\xampp\htdocs\GraduationProject\Videos\Demo1.mp4").subclip(10, 100)

# It will write the audio in converted_audio.wav file.
clip.audio.write_audiofile(r"Converted_audio.wav")
print("Finished the convertion into audio...")

filename = (r"Converted_audio.wav")

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "

                #Sentiment Analysis
                blob = TextBlob(text)
                sentiment = blob.sentiment.polarity
                if sentiment >0:
                    result= "pos"
                elif sentiment <0:
                    result= "neg"
                else:
                    result = "neutral"

                print(chunk_filename, ":", text, ", Sentiment:", result)

                whole_text += text


    analysis = TextBlob(whole_text).sentiment
    print("Full text ",analysis)
                
    # return the text for all chunks detected
    return whole_text + "(" + result + ")"
    
path = r'C:\xampp\htdocs\GraduationProject\Converted_audio.wav'
print("\nFull text:", get_large_audio_transcription(path))












