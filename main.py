import speech_recognition as sr
import webbrowser
import pyttsx3

import songLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = songLibrary.music[song]
        webbrowser.open(link)


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)

                if(word.lower() == "jarvis"):
                    speak("Yes, How I can help you")

                    with sr.Microphone() as source:
                        print("Active Jarvis...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))