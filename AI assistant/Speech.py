import pyttsx3
mouth = pyttsx3.init()
brain = "hello goodmorning"

mouth.setProperty("rate", 170)
voices = mouth.getProperty('voices')
mouth.setProperty('voice', voices[1].id)
mouth.say(brain)
mouth.runAndWait()