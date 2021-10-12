import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from pyttsx3 import engine


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis sir. Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        quary = r.recognize_google(audio, language='en-in')
        print(f"User said: {quary}\n")

    except Exception as e:
        # print(e)
       
        print("say that again please...")
        return "None"  

    return quary
if __name__ == "__main__":
    # speak("alihasan is good boy")
    wishme()
    while True:
        quary = takeCommand().lower()
        # Logic for excuting tasks based on query
        if 'wikipedia' in quary:
            speak('Searching wikipedia...')
            quary = quary.replace("wikipedia", "")
            results = wikipedia.summary(quary, sentences=2)
            speak("Accordin to wikipedia")
            speak(results)
