import datetime
from pathlib import Path
from tkinter import *
from turtle import width
from tkVideoPlayer import TkinterVideo
from tkvideo import tkvideo
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./display_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Movie_Name(x):
    return x

Movie = Movie_Name("VideoTest.mp4")

def update_duration(event):
    """ updates the duration after finding the duration """
    duration = vid_player.video_info()["duration"]
    end_time["text"] = str(datetime.timedelta(seconds=duration))
    progress_slider["to"] = duration


def update_scale(event):
    """ updates the scale value """
    progress_slider.set(vid_player.current_duration())


def seek(event=None):
    """ used to seek a specific timeframe """
    vid_player.seek(int(progress_slider.get()))


def skip(value: int):
    """ skip seconds """
    vid_player.seek(int(progress_slider.get())+value)
    progress_slider.set(progress_slider.get() + value)


def play_pause():
    """ pauses and plays """
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"

    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"


def video_ended(event):
    """ handle video ended """
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    progress_slider.set(0)

window = Tk()
window.title('Filtered Video')
window.geometry("1440x689")
window.configure(bg = "#FFFFFF")

########################################################################


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 689,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    720.0,
    344.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    195.0,
    75.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    79.0,
    72.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1262.0,
    67.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1325.0,
    65.0,
    image=image_image_5
)

########################################################################

vid_player = TkinterVideo(master=window)
vid_player.load(Movie)
vid_player.pack(side="top", fill="both", expand="yes", padx=200,
			pady=(120, 10))
#vid_player.place(relx=0.8, rely=0.5, anchor=CENTER)
vid_player.play()

play_pause_btn = tk.Button(window, text="Play", command=play_pause)
play_pause_btn.pack()

skip_plus_5sec = tk.Button(window, text="<<", command=lambda: skip(-5))
skip_plus_5sec.pack(side="left")

start_time = tk.Label(window, text=str(datetime.timedelta(seconds=0)))
start_time.pack(side="left")

progress_slider = tk.Scale(window, from_=0, to=0, orient="horizontal")
progress_slider.bind("<ButtonRelease-1>", seek)
progress_slider.pack(side="left", fill="x", expand=True)

end_time = tk.Label(window, text=str(datetime.timedelta(seconds=0)))
end_time.pack(side="left")

vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended )

skip_plus_5sec = tk.Button(window, text=">>", command=lambda: skip(5))
skip_plus_5sec.pack(side="left")

window.resizable(False, False)
window.mainloop()