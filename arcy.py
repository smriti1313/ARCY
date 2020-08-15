import pyttsx3
import speechRecognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) #hour format:24 hours
    if hour>=0 and hour<12:
        speak("Good Morning!!You woke up before 12pm.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!You gonna sleep again")
    else:
        speak("Good Evening!!Your day begins.")
    speak("ARCY at your service,your majesty!!")

if __name__=="__main__":
    wishMe()

