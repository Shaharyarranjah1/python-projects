
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import psutil
import pyjokes
import requests
import json
from bs4 import BeautifulSoup
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open Youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open Google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Music'  # Change directory as per your system
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\YourPC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Change path as per your system
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiveremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'screenshot' in query:
            pyautogui.screenshot('screenshot.png')
            speak("Screenshot taken")

        elif 'cpu' in query:
            usage = str(psutil.cpu_percent())
            speak(f'CPU usage is at {usage} percent')

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'weather' in query:
            api_key = "YOUR_API_KEY"  # Get from openweathermap.org
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Which city?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                speak(f"Temperature is {current_temperature} kelvin")
                speak(f"Pressure is {current_pressure} hectopascal")
                speak(f"Humidity is {current_humidity} percent")
            else:
                speak("City not found")

        elif 'exit' in query:
            speak("Goodbye!")
            break
