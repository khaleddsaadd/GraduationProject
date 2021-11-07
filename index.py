import nltk
from nltk.chat.util import Chat, reflections
from gtts import gTTS
import os
import random
import re
import numpy as np
import cv2
def textToSpeach(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("Bot.mp3")
    # Playing the converted file
    os.system("Bot.mp3")
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello|welcome",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["Pouney",]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"who are your Developers?",
        ["Khaled,Mai,Reem,Ahmed",]
    ],
    [
        r"What can you do?",
        ["I take your uploaded video and I can tell you what does it contain in details, and I can cut the scenes you dont want to see and I give you back a new video"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.)raining in (.)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.) health(.)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"Is (.)(appropriate|suitable) (.) (kids|children)?",
        ["Yes","No"]
    ],
    [
        r"What (.) (genre|type) (.) (movie|film)?",
        ["The Genre of the movie is ...."]
    ],
    [
        r"Where (.) (movie|film) (.) place?",
        ["The movie is  ...."]
    ],
    [
        r"Where (.*) (movie|film) produced?",
        ["The movie is produced in ...."]
    ],
    [
        r"What (.) age (.) (movie|film)?",
        ["Suggested 10+"]
    ],
    [
        r"When (.) (movie|film) (.) produced?",
        ["The video was produced in ..."]
    ],
    [
        r"what (.)last (movie|film) (.) watched?",
        ["The last movie you watched is ..."]
    ],
    [
        r"(.)Trailer (.) available?",
        ["The movie isn't released yet"]
    ],
    [
        r"What (.*)last (movie|film) released?",
        ["The last movie released in ..."]
    ],
    [
        r"what (.*) (rating)?",
        ["The movie has rating 5.5"]
    ],
    [
        r"who (.*) (director)?",
        ["The director is..."]
    ],    
    [
        r"Are (.) (Captions|Subtitles) (.) available ?",
        ["Yes","No"]
    ],
    [
        r"Is (.*) available ?",
        ["Yes","No","Not released yet"]
    ],
    [
        r"Does (.) (movie|film) (.) Sex scenes?",
        ["Yes","No"]
    ],    
    [
        r"Does (.) (movie|film) (.) (insults|Bad words)?",
        ["Yes","No"]
    ],    
    
    [
        r"bye",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
   
]
class Chat:
    def _init_(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                return resp


    # Hold a conversation with a chatbot
    def converse(self, quit="quit"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try:
                user_input = input(">")
                if user_input=="I want to upload a new video":
                    inp_video()
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                x=self.respond(user_input)
                textToSpeach(x)
def chat():
    chat = Chat(pairs, reflections)
    chat.converse()
def inp_video():
    inputvideo = input("Enter your video name \n")
    cap = cv2.VideoCapture(r'C:\xampp\htdocs\GraduationProject'+inputvideo+'.mp4')
    if (cap.isOpened()== False): 
        print("Error opening video  file")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
        
            # Display the resulting frame
            cv2.imshow('Frame', frame)
        
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        # Break the loop
        else: 
            break


if __name__ == "__main__":
    mytext = 'Welcome'
    chat()