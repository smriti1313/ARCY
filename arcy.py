import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  # hour format:24 hours
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
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

    except Exceptions as e:
        # print(e) it will print the error which will kinda look ugly
        print("Please Repeat...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    # logic for executing tasks based on query



