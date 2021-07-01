import pyttsx3
import random
import pyaudio
import requests, json
import os
import playsound
import speech_recognition as sr
import sys
import ctypes
import wikipedia
import re
import webbrowser
import smtplib
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from datetime import date, datetime, time

wikipedia.set_lang('en')
language = 'en'
path = ChromeDriverManager().install()

ear = sr.Recognizer()
mouth = pyttsx3.init()
brain = ""

def ans(you):
    if "hello" in you:
        day_time = int(strftime('%H'))
        if day_time < 7:
            brain = (random.choice(("Good morning! need any help for start a new day?")))
        if 9 < day_time < 10:
            brain = (random.choice(("Hello, do you need any help?","Hi there!")))
        if 12 < day_time < 13:
            brain = (random.choice(("Good afternoon, let's start an active afternoon!")))
        else:
            brain = (random.choice(("Hello.","Hi there!")))
    elif "goodnight" in you:
        brain = (random.choice(("Goodnight.","See you in the morning.","Talk to you in the morning.","Goodnight. See you in the morning.")))
    elif "sing" in you:
        brain = (random.choice(("I'm not a great singer, but I can help you check time if you ask.","I'm not really good at sing but I can help you check a date.")))
    elif "can you do" in you:
        brain = "I can help a lot of things like check time, date. Let's try 'What time is it?' "
    else:
        brain = (random.choice(("I didn't understand what you're saying, please try again.","Sorry, I'm not able to help with this one.", "Sorry I can't help you with that, I'm still learing.")))

def time(you):
    if "today" in you:
        today = date.today()
        brain = "Today is " + today.strftime("%A %B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        brain = "Now is " + now.strftime("%H:%M %p")

def bye(you):
    brain = (random.choice(('Goodbye, see you later.','Ok Goodbye.',"I'll be standing by.")))
    print("A.M.U.R: " + brain)
    mouth.setProperty("rate", 170)
    voices = mouth.getProperty('voices')
    mouth.setProperty('voice', voices[1].id)
    mouth.say(brain)
    mouth.runAndWait()
    

while True:
    with sr.Microphone() as mic:
        ear.adjust_for_ambient_noise(mic) 
        print("A.M.U.R: I'm listening...")
        audio = ear.listen(mic)

    print("A.M.U.R: ...")

    try:
        you = ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if you == "":
        brain = "I can't hear you, please try again."
    elif "time" or "today" in you:
        brain = time(you)
    elif "bye" in you:
        bye(you)
        break 
    else:
        brain = ans(you)
        
    print("A.M.U.R: " + brain)

    mouth.setProperty("rate", 170)
    voices = mouth.getProperty('voices')
    mouth.setProperty('voice', voices[1].id)
    mouth.say(brain)
    mouth.runAndWait()