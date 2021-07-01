import speech_recognition
import pyttsx3
import random
import pyaudio
import requests, json
import webbrowser
import os
from datetime import date, datetime, time

ear = speech_recognition.Recognizer()
mouth = pyttsx3.init()
brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        ear.adjust_for_ambient_noise(mic) 
        print("Assistant: I'm listening...")
        audio = ear.listen(mic)

    print("Assistant: ...")

    try:
        you = ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if you == "":
        brain = "I can't hear you, please try again."
    elif "hello" in you:
        brain = (random.choice(("Hello, nice to see you again!","Hi! do you need any help?")))
    elif "goodnight" in you:
        brain = (random.choice(("Goodnight.","See you in the morning.","Talk to you in the morning.","Goodnight. See you in the morning.")))
    elif "today" in you:
        today = date.today()
        brain = "Today is " + today.strftime("%A %B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        brain = "Now is " + now.strftime("%H:%M %p")
    elif "sing" in you:
        brain = (random.choice(("I'm not a great singer, but I can help you check time if you ask.","I'm not really good at sing but I can help you check a date.")))
    elif "can you do" in you:
        brain = "I can help a lot of things like check time, date. Let's try 'What time is it?' "
    elif "bye" in you:
        brain = (random.choice(('Goodbye, see you later.','Ok Goodbye.',"I'll be standing by.")))
        print("Assistant: " + brain)
        mouth.setProperty("rate", 170)
        voices = mouth.getProperty('voices')
        mouth.setProperty('voice', voices[1].id)
        mouth.say(brain)
        mouth.runAndWait()
        break
    else:
        brain = (random.choice(("I didn't understand what you're saying, please try again.","Sorry, I'm not able to help with this one.", "Sorry I can't help you with that, I'm still learing.")))
    
    print("Assistant: " + brain)

    mouth.setProperty("rate", 170)
    voices = mouth.getProperty('voices')
    mouth.setProperty('voice', voices[1].id)
    mouth.say(brain)
    mouth.runAndWait()