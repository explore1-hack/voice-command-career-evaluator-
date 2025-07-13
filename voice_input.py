import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now.")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("🤷 Could not understand audio")
            return ""
        except sr.RequestError:
            print("⚠️ Could not request results, check internet")
            return ""
