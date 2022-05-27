from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from cgitb import text
from email import message
import tkinter.font as font
from numpy import size
from regex import E, P
import pyrebase
import json
from tkinter import messagebox
from tkinter.ttk import *
from urllib3.exceptions import HTTPError as BaseHTTPError
from pathlib import Path
from tkinter import *
from turtle import bgcolor, color, home
from tkinter import filedialog
import sys
sys.path.append('Subtitle Emotions')
from OneSubtitleEmotions import OneSubtitleEmotions
from matching_uploaded_pre import match
from BlurScene import *
from tkVideoPlayer import TkinterVideo
from tkvideo import tkvideo
import datetime

global my_text
global my_text_2   
MovieName=""
SubtitlesName=""

OUTPUT_PATH =Path(__file__).parent
config = {'apiKey': "AIzaSyD3SaqfyUcu1Xnjkeaqw3ILpn_w4v5s4Fo",
  'authDomain': "pruney-4e073.firebaseapp.com",
  'databaseURL':"https://pruney-4e073.firebaseapp.com",
  'projectId': "pruney-4e073",
  'storageBucket': "pruney-4e073.appspot.com",
  'messagingSenderId': "969307424804",
  'appId': "1:969307424804:web:f6706080c47108567430b1",
  'measurementId': "G-FQRT3VDG5B"}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

class Applications:
    def setApp(self,app):
        self.app= app
    def Signin(self,Email,Password):
        global my_text
        global my_text_2
        if not Email:
            print("Mail is empty")
            my_text = "Please Enter An Email"
            # EmailErr()
        elif not Password:
                print("Password is empty")
                my_text = ""
                # EmailErr()
                my_text_2 = "Please Enter Yout Password"
                # PassErr()
        else:
            try:
                signin = auth.sign_in_with_email_and_password(Email, Password)
                print("Done")
                self.app.switch_frame(input_page)
            except Exception as e:
                print("Error")
    def Signup(self,Email,Password):
        if not Email:
            my_text = "Please Enter An Email"
            # EmailErr()
        elif not Password:
            my_text = ""
            # EmailErr()
            my_text_2 = "Please Enter A Password"
            # PassErr()
        else:
            try:
                user = auth.create_user_with_email_and_password(Email, Password)
                print("Account Created")
                self.app.switch_frame(input_page)
            except Exception as e:
                print("Error")
    def browseMovie(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("video files",
                                                        ".mp4"),
                                                       ("all files",
                                                        ".")))
        if filename != "":
            # canvas.itemconfig(MovieLabel, text=filename)
            global MovieName
            MovieName = filename
            # clip = VideoFileClip(filename) 
            # clip = clip.subclip(1, 3)
            # clip.preview()
            return filename
    def browseSubtitles(self):
        SFileName = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            ".txt"),
                                                        ("all files",
                                                            ".")))
        if SFileName != "":
            # canvas.itemconfig(SubtitleLabel, text=SFileName)
            global SubtitlesName
            SubtitlesName = SFileName
            return SFileName
    def start(self):
        print("Movie Name: ",MovieName)
        print("Suvtitles Name: ",SubtitlesName)
        result = OneSubtitleEmotions(SubtitlesName)
        Sequence_emotions= result[0]
        Time_emotions = result[1]
        print("Subtitles Emotions",Sequence_emotions)
        print("Subtitles Times",Time_emotions)
        n = 30
        def divide_chunks(l, n):
            count = 0
            for i in range(0, len(l), n): 
                yield l[i:i + n]
        Subsequences = list(divide_chunks(Sequence_emotions, n))
        SubTime = list(divide_chunks(Time_emotions, n))
        for (subE, subT) in zip(Subsequences, SubTime):
            match(Sequence_emotions,subE,subT,MovieName)
        Blurring_Violence_CSV(MovieName)
        FinalPath = Blurring_Violence_CSV(MovieName)
        self.app.switch_frame(Display)
    def setHomePath(self, path:str) -> Path:
        ASSETS_PATH = OUTPUT_PATH / Path("./home_assets")
        return ASSETS_PATH / Path(path)
    def setSignPath(self, path:str) -> Path:
        ASSETS_PATH = OUTPUT_PATH / Path("./signin_assets")
        return ASSETS_PATH / Path(path)
    def setSignupPath(self, path:str) -> Path:
        ASSETS_PATH = OUTPUT_PATH / Path("./signup_assets")
        return ASSETS_PATH / Path(path)
    def setinputPath(self, path:str) -> Path:
        ASSETS_PATH = OUTPUT_PATH / Path("./input_assets")
        return ASSETS_PATH / Path(path)
    def setdisplaypath(self, path:str) -> Path:
        ASSETS_PATH = OUTPUT_PATH / Path("./display_assets")
        return ASSETS_PATH / Path(path)

App_instance = Applications()

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1440x689")
        self.configure(bg = "#FFFFFF")
        self.frame=None
        self.switch_frame(home)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        
class home(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        canvas = Canvas(
        bg = "#FFFFFF",
        height = 689,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1440.0,
            689.0,
            fill="#6079BD",
            outline="")

        canvas.create_rectangle(
            0.0,
            0.0,
            600,
            800,
            fill="#F7FFFF",
            outline="")

        image_image_1 = PhotoImage(
            file=App_instance.setHomePath("image_1.png"))
        image_1 = canvas.create_image(
            302.0,
            301.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=App_instance.setHomePath("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=50,
            highlightthickness=50,
            command=lambda:master.switch_frame(sign_in),
            relief="flat"
        )
        button_1.place(
            x=158.0,
            y=484.0,
            width=113.0,
            height=42.0
        )

        canvas.create_text(
            158.0,
            543.0,
            anchor="nw",
            text="Don't have an accout?\n",
            fill="#10105E",
            font=("Roboto Thin", 14 * -1)
        )

        button_image_2 = PhotoImage(
            file=App_instance.setHomePath("button_2.png"))
        button_2 = Button (
            # text="Sign Up",
            # font=("Roboto Medium", 14 * -1),
            image=button_image_2,
            borderwidth=20,
            highlightthickness=0,
            command=lambda:master.switch_frame(sign_up),
            relief="flat"
        )
        button_2.place(
            x=158.0,
            y=564.0,
            width=49.0,
            height=22.0
        )

        image_image_2 = PhotoImage(
            file=App_instance.setHomePath("image_2.png"))
        image_2 = canvas.create_image(
            720.0,
            331.0,
            image=image_image_2
        )
        App_instance.setApp(master)
        master.mainloop()
class sign_in(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        canvas = Canvas(
        bg = "#FFFFFF",
        height = 689,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1440.0,
            689.0,
            fill="#6079BD",
            outline="")


        button_image_H = PhotoImage(
            file=App_instance.setSignPath("image_1.png"))
        button_H = Button(
            image=button_image_H,
            borderwidth=0,
            highlightthickness=0,
            # command=HomePage,
            relief="flat",
            bg="#6079BD",
            activebackground='#6079BD'
        )
        button_H.place(
            x=50.0,
            y=75.0,
            width=217.0,
            height=45.0
        )


        image_image_2 = PhotoImage(
            file=App_instance.setSignPath("image_2.png"))
        image_2 = canvas.create_image(
            1112.0,
            443.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=App_instance.setSignPath("image_3.png"))
        image_3 = canvas.create_image(
            376.0,
            313.0,
            image=image_image_3
        )

        button_s = Button(
            
            text="Sign Up",
            
            fg="#FFFFFF",
            bg="#6079BD",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            # command=SignUp,
            activebackground='#6079BD'
            
        )
        button_s.place(
            x=1169.0,
            y=61.0,
            width=200.0,
            height=50.0
        )
        # button_s['font'] = myFontS

        canvas.create_rectangle(
            513.0,
            123.0,
            959.0,
            655.0,
            fill="#F7FFFF",
            outline="")

        canvas.create_text(
            652.0,
            183.0,
            anchor="nw",
            text="Sign In",
            fill="#000000",
            font=("Roboto Bold", 48 * -1)
        )
        image_image_1 = PhotoImage(
            file=App_instance.setSignPath("email.png"))
        image_1 = canvas.create_image(
            580.0,
            295,
            image=image_image_1
        )
        canvas.create_text(
            601.0,
            285.0,
            anchor="nw",
            text="Email (@example.com)",
            fill="#868686",
            font=("Roboto Thin", 14 * -1)
        )

        entry_image_1 = PhotoImage(
            file=App_instance.setSignPath("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            736.0,
            345.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#F9F8F8",
            highlightthickness=0
        )
        entry_1.place(
            x=565.0,
            y=313.0,
            width=342.0,
            height=47.0
        )
        my_label = Label( text = "",
        bg="#FFFFFF",
        fg="red")

        my_label.place(
            x=565.0,
            y=382.0
        )

        image_image_p = PhotoImage(
            file=App_instance.setSignPath("pass.png"))
        image_p = canvas.create_image(
            580.0,
            415,
            image=image_image_p
        )
        canvas.create_text(
            601.0,
            405.0,
            anchor="nw",
            text="Password",
            fill="#868686",
            font=("Roboto Thin", 14 * -1)
        )

        entry_image_2 = PhotoImage(
            file=App_instance.setSignPath("entry_3.png"))
        entry_bg_2 = canvas.create_image(
            736.0,
            455.5,
            image=entry_image_2
        )

        e1_str=StringVar()
        entry_2 = Entry(
            bd=0,
            bg="#F9F8F8",
            highlightthickness=0,
            show='*',
            textvariable=e1_str
        )
        entry_2.place(
            x=565.0,
            y=430.0,
            width=342.0,
            height=47.0
        )
        c_v1=IntVar(value=0)

        def my_show():
            
            if(c_v1.get()==1):
                entry_2.config(show='')
            else:
                entry_2.config(show='*')

        c1 = Checkbutton(text='Show Password',variable=c_v1,
            onvalue=1,offvalue=0,command=my_show,bg="#FFFFFF", activebackground='#FFFFFF')

        c1.place(
            x=775.0,
            y=485.0,
            width=150.0,
            height=25.0
        )

        # c1['font'] = myFont_2
        my_label_2 = Label( 
        text = "",
        bg="#FFFFFF",
        fg="red")

        my_label_2.place(
            x=565.0,
            y=490.0
        )

        button_for = Button(
            # image=button_image_1,
            text="Forget Password?",
            fg="#A31E85",
            borderwidth=0,
            highlightthickness=0,
            # command=ResetPass,
            relief="flat",
            bg="#FFFFFF",
            activebackground='#FFFFFF'
        )
        button_for.place(
            x=678.0,
            y=510.0,
            width=117.0,
            height=45.0
        )
        # button_for['font'] = myFont

        button_image_1 = PhotoImage(
            file=App_instance.setSignPath("Group.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: App_instance.Signin(entry_1.get(),entry_2.get()),
            relief="flat",
            bg="#FFFFFF"
        )
        button_1.place(
            x=628.0,
            y=557.0,
            width=217.0,
            height=55.0
        )

        canvas.create_text(
            709.0,
            509.0,
            anchor="nw",
            text="Sign In",
            fill="#FFFFFF",
            font=("Roboto Medium", 18 * -1)
        )


        canvas.create_rectangle(
            1283.0,
            91.0,
            1329.0,
            91.0,
            fill="#000000",
            outline=""
        )    
# window.resizable(False, False)
        master.mainloop()
class sign_up(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        canvas = Canvas(
            bg = "#FFFFFF",
            height = 689,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1440.0,
            689.0,
            fill="#B44E9D",
            outline="")

        canvas.create_rectangle(
            0.0,
            0.0,
            552.0,
            820.0,
            fill="#F7FFFF",
            outline="")

        button_image_1 = PhotoImage(
            file=App_instance.setSignupPath("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            
            fg="#313072",
            bg="#B44E9D",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            # command=HomePage,
            activebackground='#B44E9D'
            
        )
        button_1.place(
            x=569.0,
            y=61.0,
            width=200.0,
            height=50.0
        )

        # button_image_2 = PhotoImage(
        #     file=relative_to_assets("button_2.png"))
        button_2 = Button(
            # image=button_image_2,
            text="Sign In",
            bg="#B44E9D",
            fg='#000000',
            borderwidth=0,
            highlightthickness=0,
            # command=SignInPage,
            relief="flat"
        )
        button_2.place(
            x=1276.0,
            y=65.0,
            width=65.0,
            height=31.0
        )
        # button_2['font'] = myFont
        canvas.create_text(
            122.0,
            94.0,
            anchor="nw",
            text="Sign Up",
            fill="#000000",
            font=("Roboto Bold", 48 * -1)
        )

        image_image_1 = PhotoImage(
            file=App_instance.setSignupPath("image_1.png"))
        image_1 = canvas.create_image(
            136.0,
            238,
            image=image_image_1
        )

        canvas.create_text(
            160.0,
            230,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Roboto Thin", 14 * -1)
        )


        entry_image_1 = PhotoImage(
            file=App_instance.setSignupPath("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            285.0,
            280.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#F9F8F8",
            highlightthickness=0
        )
        entry_1.place(
            x=114.0,
            y=256.0,
            width=342.0,
            height=47.0
        )
        my_label = Label( text = "",
        bg="#FFFFFF",
        fg="red")

        my_label.place(
            x=114.0,
            y=310.0
        
        )

        image_image_2 = PhotoImage(
            file=App_instance.setSignupPath("image_2.png"))
        image_2 = canvas.create_image(
            136.0,
            350.0,
            image=image_image_2
        )


        canvas.create_text(
            160.0,
            340.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Roboto Thin", 14 * -1)
        )
        entry_image_2 = PhotoImage(
            file=App_instance.setSignupPath("entry_1.png"))

        entry_bg_2 = canvas.create_image(
            285.0,
            400.0,
            image=entry_image_2
        )

        e1_str=StringVar()
        entry_2 = Entry(
            bd=0,
            bg="#F9F8F8",
            highlightthickness=0,
            show='*',
            textvariable=e1_str
        )

        entry_2.place(
            x=114.0,
            y=367.0,
            width=342.0,
            height=47.0
        )

        c_v1=IntVar(value=0)

        def my_show():
            
            if(c_v1.get()==1):
                entry_2.config(show='')
            else:
                entry_2.config(show='*')

        c1 = Checkbutton(text='Show Password',variable=c_v1,
            onvalue=1,offvalue=0,command=my_show,bg = "#FFFFFF",)

        c1.place(
            x=70.0,
            y=450.0,
            width=200.0,
            height=45.0
        )

        # c1['font'] = myFont_2

        my_label_2 = Label( text = "",
        bg="#FFFFFF",
        fg="red")

        my_label_2.place(
            x=114.0,
            y=430.0 
        )

        button_image_1 = PhotoImage(
            file=App_instance.setSignupPath("SignUp.png"))
        button_1 = Button(
            image=button_image_1,
            bg = "#FFFFFF",
            fg='#B44E9D',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: App_instance.Signup(entry_1.get(),entry_2.get()),
            relief="flat",
            
        )
        button_1.place(
            x=150.0,
            y=500.0,
            width=257.0,
            height=100.0
        )
        # button_1['font'] = myFont

        image_image_3 = PhotoImage(
            file=App_instance.setSignupPath("image_3.png"))
        image_3 = canvas.create_image(
            1182.0,
            405.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=App_instance.setSignupPath("image_4.png"))
        image_4 = canvas.create_image(
            824.0,
            622.0,
            image=image_image_4
        )

        # image_image_5 = PhotoImage(
        #     file=relative_to_assets("image_5.png"))
        # image_5 = canvas.create_image(
        #     137.0,
        #     433.0,
        #     image=image_image_5
        # )

        # image_image_6 = PhotoImage(
        #     file=relative_to_assets("image_6.png"))
        # image_6 = canvas.create_image(
        #     137.0,
        #     272.0,
        #     image=image_image_6
        # )

        # image_image_7 = PhotoImage(
        #     file=relative_to_assets("image_7.png"))
        # image_7 = canvas.create_image(
        #     137.0,
        #     351.0,
        #     image=image_image_7
        # )
        master.mainloop()
class input_page(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        label_file_explorer = Label(
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
        label_file_explorer_2 = Label(
                                    text = "File Explorer using Tkinter",
                                    width = 100, height = 4,
                                    fg = "blue")

        canvas = Canvas(
            bg = "#FFFFFF",
            height = 689,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=App_instance.setinputPath("image_1.png"))
        image_1 = canvas.create_image(
            720.0,
            344.0,
            image=image_image_1
        )


        image_image_2 = PhotoImage(
            file=App_instance.setinputPath("image_2.png"))
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
            file=App_instance.setinputPath("image_3.png"))
        image_3 = canvas.create_image(
            1262.0,
            67.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=App_instance.setinputPath("image_4.png"))
        image_4 = canvas.create_image(
            1325.0,
            65.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=App_instance.setinputPath("image_5.png"))
        image_5 = canvas.create_image(
            441.0,
            391.0,
            image=image_image_5
        )
        #hena 



        canvas.create_rectangle(
            824.0,
            453.0,
            1267.0,
            510.0,
            fill="#FFFFFF",
            outline="")

        #Upload Button
        button_image_1 = PhotoImage(
            file=App_instance.setinputPath("image_6.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            text="button_1 clicked",
            command=lambda: App_instance.browseMovie(),
            relief="flat"
        )
        button_1.place(
            x=1177.0,
            y=460.0,
            width=88.0,
            height=50.0
        )



        canvas.create_rectangle(
            824.0,
            453.0,
            1267.0,
            610.0,
            fill="#FFFFFF",
            outline="")    
        button_image_2 = PhotoImage(
            file=App_instance.setinputPath("image_6.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            text="button_2 clicked",
            command=lambda: App_instance.browseSubtitles(),
            relief="flat"
        )
        button_2.place(
            x=1177.0,
            y=550.0,
            width=88.0,
            height=50.0
        )

        MovieLabel = canvas.create_text(
            950.0,
            490.0,
            anchor="nw",
            text="Upload Movie File\n",
            fill="#10105E",
            font=("Roboto Thin", 14 * -1)
        )

        SubtitleLabel = canvas.create_text(
            950.0,
            570.0,
            anchor="nw",
            text="Upload Subtitles File\n",
            fill="#10105E",
            font=("Roboto Thin", 14 * -1)
        )

        button_s = Button(
            
            text="Start Filtering",
            fg="#000000",
            bg="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: App_instance.start(),
            relief="flat",
            activebackground='#6079BD'
            
        )
        button_s.place(
            x=960.0,
            y=630.0,
            width=200.0,
            height=20.0
        
        )
        master.mainloop()
class Display(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        canvas = Canvas(
            bg = "#FFFFFF",
            height = 689,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=App_instance.setdisplaypath("image_1.png"))
        image_1 = canvas.create_image(
            720.0,
            344.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=App_instance.setdisplaypath("image_2.png"))
        image_2 = canvas.create_image(
            195.0,
            75.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=App_instance.setdisplaypath("image_3.png"))
        image_3 = canvas.create_image(
            79.0,
            72.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=App_instance.setdisplaypath("image_4.png"))
        image_4 = canvas.create_image(
            1262.0,
            67.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=App_instance.setdisplaypath("image_5.png"))
        image_5 = canvas.create_image(
            1325.0,
            65.0,
            image=image_image_5
        )

        # def Movie_Name(x):
        #     return x

        # Movie 

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


        vid_player = TkinterVideo(master)
        vid_player.load(MovieName)
        vid_player.pack(side="top", fill="both", expand="yes", padx=200,
                    pady=(120, 10))
        #vid_player.place(relx=0.8, rely=0.5, anchor=CENTER)
        vid_player.play()

        play_pause_btn = Button(master, text="Play", command=play_pause)
        play_pause_btn.pack()

        skip_plus_5sec = Button(master, text="<<", command=lambda: skip(-5))
        skip_plus_5sec.pack(side="left")

        start_time = Label(master, text=str(datetime.timedelta(seconds=0)))
        start_time.pack(side="left")
        progress_slider = Scale(master, from_=0, to=0, orient="horizontal")
        progress_slider.bind("<ButtonRelease-1>", seek)
        progress_slider.pack(side="left", fill="x", expand=True)

        end_time = Label(master, text=str(datetime.timedelta(seconds=0)))
        end_time.pack(side="left")

        vid_player.bind("<<Duration>>", update_duration)
        vid_player.bind("<<SecondChanged>>", update_scale)
        vid_player.bind("<<Ended>>", video_ended )

        skip_plus_5sec = Button(master, text=">>", command=lambda: skip(5))
        skip_plus_5sec.pack(side="left")

        master.mainloop()

app=SampleApp()