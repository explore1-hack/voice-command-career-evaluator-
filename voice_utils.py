import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "API error. Try again."
