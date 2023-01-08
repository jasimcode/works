import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


while True:
    speak("Hello Mr Jasim this is friday")
