from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[2].id)

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning,Dheemanth.")
    elif hour>=12 and hour<=16:
        speak("Good afternoon,Dheemanth.")
    else:
        speak("Good evening,Dheemanth.")

    speak("I am Scar. Please let me know how can I assist you")

def takeCommand():
    # It takes microphone input from the user and returns a string output
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source) 

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query







if __name__ == "__main__":
    # speak("Dheemanth is a good boy")
    wishMe()
    takeCommand()
