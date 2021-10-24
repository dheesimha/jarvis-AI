from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

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
        speak("Good morning boss.")
    elif hour>=12 and hour<=16:
        speak("Good afternoon boss.")
    else:
        speak("Good evening boss.")

    speak("I am Jarvis. Please let me know how can I assist you")

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
    wishMe()
    while True:
        query = takeCommand().lower()


    # Logic for executing tasks based on queries 

    # Wikipedia : Jarvis reads out the summary from wikipedia
       
        if 'wikipedia' in query:
            speak("searching wikipedia..." )
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
    
    # To exit jarvis
        elif 'exit' in query:
            speak("Over and out boss!Have a great time")
            break
    

    # To open youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        


