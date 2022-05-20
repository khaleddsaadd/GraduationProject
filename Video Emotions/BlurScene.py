import cv2
import csv
import numpy as np
from csv import reader

import pandas as pd
from moviepy.video.compositing.concatenate import concatenate_videoclips
from skimage.filters import gaussian
from moviepy.editor import VideoFileClip, clips_array, concatenate_videoclips
from moviepy.editor import VideoFileClip, concatenate_videoclips

def blur(image):
    return cv2.medianBlur(image, 101)
def BlurringPart(MovieName,Start,End):
    BeforeViolnce = Start-1
    PostViolence = End+1
    clip = VideoFileClip(MovieName,".mp4")
    # x =int(clip.duration)
    # count=0
    # clips=[]
    # for i in range(0,clip.duration()):
    #     if(i==Start[i]):
    #         clip[i].subclip(Start[i],End[i])
    #         clip[i].preview()
    clip1 = VideoFileClip(MovieName,".mp4").subclip(clip.start,BeforeViolnce)
    clip2 = VideoFileClip(MovieName,".mp4").subclip(Start,End)
    clip3 = VideoFileClip(MovieName,".mp4").subclip(PostViolence,clip.end)
    clip2_blurred = clip2.fl_image(blur)
    final_clip = concatenate_videoclips([clip1,clip2_blurred,clip3])

def Violence_CSV(MovieName):
    Start=[]
    End=[]
    print("Maioi: ",MovieName)
    MovieName_CSV = MovieName + ".csv"
    print(MovieName_CSV)
    with open(MovieName_CSV, 'r') as my_file:
        file_csv = reader(my_file)
        head = next(file_csv)
        if head is not None:
            for i in file_csv:
                Start.append(i[0])
                End.append(i[1])
    print(Start)
    print(End)
    # for i in range (len(Start)):
    #     print(Start[i])
    #     BlurringPart(MovieName,int(Start[i]),int(End[i]))
    # BlurringPart(MovieName,Start,End)
Violence_CSV("F:\Films and Series\[EgyBest].Mr.Nobody.2009.BluRay.720p.x264.mp4")
# BlurringPart(MovieName,int(Start[i]),int(End[i]))