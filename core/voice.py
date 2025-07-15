import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="en-US")
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        return "Sorry, I didn't get that."

def start_listening():
    while True:
        command = listen()
        if command:
            speak(f"You said: {command}")
