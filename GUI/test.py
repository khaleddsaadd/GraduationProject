from tkinter import *
from tkvideo import tkvideo
# create instance fo window
root = Tk()
# set window title
root.title('Video Player')
# create label
video_label = Label(root)
video_label.pack()
# read video to display on label
player = tkvideo(r"C:\xampp\htdocs\GraduationProject\VideoTest.mp4", video_label,
                 loop = 1, size = (700, 500))
player.play()
root.mainloop()

