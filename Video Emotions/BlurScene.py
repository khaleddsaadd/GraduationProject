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
# def BlurringPart(MovieName,Start,End):
    # clip = VideoFileClip(MovieName)
    # # clip1 = VideoFileClip(MovieName.subclip(clip.start,Start[0])
    # # clip2 = VideoFileClip(MovieName,)

    # print(Start)
    # print(End)
    # BeforeViolnce = Start-1
    # PostViolence = End+1
    # x =int(clip.duration)
    # count=0
    # clips=[]
    # for i in range(0,clip.duration()):
    #     if(i==Start[i]):
    #         clip[i].subclip(Start[i],End[i])
    #         clip[i].preview()
    # clip1 = VideoFileClip(MovieName,".mp4").subclip(clip.start,BeforeViolnce)
    # clip2 = VideoFileClip(MovieName,".mp4").subclip(Start,End)
    # clip3 = VideoFileClip(MovieName,".mp4").subclip(PostViolence,clip.end)
    # clip2_blurred = clip2.fl_image(blur)
    # final_clip = concatenate_videoclips([clip1,clip2_blurred,clip3])

def Blurring_Violence_CSV(MovieName):
    clip = VideoFileClip(MovieName)
    # clip1 = VideoFileClip(MovieName.subclip(clip.start))
    begin = 0
    Start=[]
    End=[]
    print("Movie Name: ",MovieName)
    MovieName_CSV = MovieName + ".csv"
    print(MovieName_CSV)
    with open(MovieName_CSV, 'r') as my_file:
        file_csv = reader(my_file)
        head = next(file_csv)
        if head is not None:
            for i in file_csv:
                Start.append(i[0])
                End.append(i[1])
                w = clip.subclip(begin,int(i[0]))
                # begin = i[1]
                # print(w.start ,"  ", w.end)
                # x = clip.subclip(i[0],i[1])
                # print(x.start," ",x.end)
                # begin = int(i[1]) + 1
                # b = x.fl_image(blur)
                # b.preview()
    print(Start)
    print(End)
    clips = []
    for i in range(len(Start)):
        print("Normal: ", begin,Start[i])
        print("Violence: ", Start[i],End[i])
        x=clip.subclip(begin,Start[i])
        y=clip.subclip(Start[i],End[i]).fl_image(blur)
        begin = int(End[i]) 
        clips.append(x)
        clips.append(y)
        
    print("Normal: ",End[i],clip.end)
    z=clip.subclip(End[i],clip.end)
    clips.append(z)
    final = concatenate_videoclips(clips)
 
# showing final clip
    final.ipython_display(width = 480)
    
    
    # final_clip = concatenate_videoclips([clips])
    # final_clip.preview()

Blurring_Violence_CSV("F:\Films and Series\[EgyBest].Mr.Nobody.2009.BluRay.720p.x264.mp4")

# BlurringPart(MovieName,int(Start[i]),int(End[i]))