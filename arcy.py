import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  # hour format:24 hours
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("ARCY at your service,your majesty!!")


def takeCommand():
    # it takes in microphone input from the user and returns and string output
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        # print("User said: ", query)
        print(f"User said: {query}\n")

    except Exception:  # except Exceptions as e
        # print(e) it will print the error which will kinda look ugly
        print("Please Repeat...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open twitter' in query:
            webbrowser.open('twitter.com')

        elif 'tokyo ghoul' in query:
            vid="C:\\Users\\Smriti\\Desktop\\college\\tokyo ghoul s2"
            vi=os.listdir(vid)
            print(vi)
            os.startfile(os.path.join(vid, vi[0]))

        elif 'time' in query:
            string = datetime.datetime.now().strftime("%M:%M:%S")
            speak (string)

