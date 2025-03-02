# create a weather app that takes in a city name and returns the weather

from tkinter import * 
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        timezone = pytz.timezone(result)
        local_time = datetime.now(timezone)
        current_time = local_time.strftime("%I:%M %p")
        
        # Weather API
        api_key = "b416ff7f0ed707ff29a56c23427f79f9"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        # Update Labels
        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | FEELS LIKE {temp}°C")
        
        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)
        d.config(text=description)
        time_label.config(text=current_time)
        
    except Exception as e:
        print("Error:", e)

# Search Box
Search_image = PhotoImage(file="")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
time_label = Label(root, font=("Helvetica", 20))
time_label.place(x=30, y=100)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=450, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=650, y=430)


root.mainloop()