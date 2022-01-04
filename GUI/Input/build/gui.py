
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x689")
window.configure(bg = "#FFFFFF")


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

canvas.create_rectangle(
    66.0,
    63.0,
    92.0,
    67.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    66.0,
    70.0,
    92.0,
    74.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    66.0,
    77.0,
    92.0,
    81.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1262.0,
    67.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1325.0,
    65.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    441.0,
    391.0,
    image=image_image_5
)

canvas.create_rectangle(
    824.0,
    453.0,
    1267.0,
    510.0,
    fill="#FFFFFF",
    outline="")

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1216.5,
    482.5999755859375,
    image=image_image_6
)

canvas.create_rectangle(
    1194.0,
    460.0,
    1239.0,
    504.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
