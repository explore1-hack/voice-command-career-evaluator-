import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Speed of voice
engine.setProperty('volume', 1.0)  # Volume 0-1

def speak(text):
    engine.say(text)
    engine.runAndWait()
    return engine.lower(text)


