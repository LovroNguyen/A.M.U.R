import requests, json
import speech_recognition
import pyttsx3

ear = speech_recognition.Recognizer()

def weather(city_name):
    api_key = "b753dab7bc67ca48243e683212a1167a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        у = data["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = data["weather"]
        weather_description = z[0]["description"]
        brain = "Right now is " + str(weather_description) , "Temperature is " + str(current_temperature) + " C, " + "and Current humidiy is" + str(current_humidiy) + "%"
    else:
        brain = "Can't find the name of city."
    return brain

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

if "weather" in you:
    brain = "Tell me the name of city."
    print("Assistant: " + brain)
    you = 
    print("You search: " + you)
    brain = weather(you)
    if "Can't find the name of city." in brain:
        you = input("Assistant: Type a name of city: ")
        brain = weather(you)

print("Assistant: " + brain)