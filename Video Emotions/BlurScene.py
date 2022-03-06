import cv2
import numpy as np
from moviepy.video.compositing.concatenate import concatenate_videoclips
from skimage.filters import gaussian
from moviepy.editor import VideoFileClip, clips_array, concatenate_videoclips
from moviepy.editor import VideoFileClip, concatenate_videoclips
def blur(image):
    return cv2.medianBlur(image, 101)
def BlurringPart(Start,End):
    BeforeViolnce = Start-1
    PostViolence = End+1
    clip1 = VideoFileClip("VideoTest.mp4").subclip(1,BeforeViolnce)
    clip2 = VideoFileClip("VideoTest.mp4").subclip(Start,End)
    clip3 = VideoFileClip("VideoTest.mp4").subclip(PostViolence,15)
    clip2_blurred = clip2.fl_image(blur)
    final_clip = concatenate_videoclips([clip1,clip2_blurred,clip3])
    final_clip.write_videofile("my_concatenation.mp4")
    cap = cv2.VideoCapture('my_concatenation.mp4')
    if (cap.isOpened()== False): 
        print("Error opening video  file")
    while(cap.isOpened()): 
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else: 
            break
    cap.release()
    cv2.destroyAllWindows()
BlurringPart(5,10)

