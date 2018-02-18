# Import the required module for text
# to speech conversion
from gtts import gTTS
import datetime

# This module is imported so that we can
# play the converted audio
import os
def func(mytext):
    # The text that you want to convert to audio


    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    sound=mytext.replace(" ","")
    myobj.save(sound+".mp3")

    # Playing the converted file
    os.system(sound+".mp3")
mytext=input("Text to speech\nType Something: ")

func(mytext)
a=int(input("Press 1 to continue else 0 : "))
while a==1:
    back=input("Text to speech\nType Something: ")

    func(back)
    a=int(input("Press 1 to continue else 0 : "))
