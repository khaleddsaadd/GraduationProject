# Import everything needed to edit video clips 
from moviepy.editor import *
     
clip = VideoFileClip("Video Emotions\\Jamesbond.mp4")       

#clip = clip.subclip(0, 40) 

clip = clip.cutout(15, 20)
clip.write_videofile("FilteredMovie.mp4")
clip.ipython_display(width = 360,autoplay=True,maxduration=500)