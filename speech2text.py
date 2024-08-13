import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Checking ambient noise...")
    recognizer.adjust_for_ambient_noise(source)
    print("Speak now...")
    audio = recognizer.listen(source)


try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print("You said:" + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")