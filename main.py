from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import requests
import json
import tkinter as tk
import random
import pytz
from  geopy.geocoders import Photon
from timezonefinder import TimezoneFinder
from datetime import datetime


window = tk.Tk()
api_key = "00beef8fc9c995b42a522b5f790ee829"

# Set the default window size
default_width = 900
default_height = 500
window.geometry(f"{default_width}x{default_height}+300+200")
window.resizable(False,False)


def search():
    text = textField.get()
    geolocator = Photon(user_agent="geoapiExercises")
    location = geolocator.geocode(text)

    obj = TimezoneFinder()
    result  =obj.timezone_at(lng = location.longitude, lat = location.latitude)


    home =pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text =current_time)
    name.config(text = "CURRENT WEATHER")



    url = f"http://api.openweathermap.org/data/2.5/weather?q={text}&APPID={api_key}"
    response = requests.get(url).json()

    condition  = response['weather'][0]['main']
    desctiption = response['weather'][0]['description']
    temp= int(response['main']['temp']-273.15)
    pressure = response['main']['pressure']
    humidity = response['main']['humidity']
    wind = response['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))


    w.config(text=wind)
    h.config(text=humidity)
    d.config(text = desctiption)
    p.config(text=pressure)






search_image = PhotoImage(file="./weather_icons/search_box.png")
search_image = search_image.subsample(2)
search_box = Label(image=search_image)
search_box.place(x=20, y=20)

textField = Entry(window, justify="center", width=17, font=("poppins", 20, "bold"), bg="#595959", border=0, fg="white")
textField.place(x=30, y=30)
textField.focus()

search_icon = PhotoImage(file="./weather_icons/search_Icon.png")
search_icon = search_icon.subsample(22)
my_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#595959", command=search)
my_icon.place(x=250, y=22)


#logo
Logo_image = PhotoImage(file = "./weather_icons/cloudy.png")
Logo_image = Logo_image.subsample(4)
logo = Label(image = Logo_image)
logo.place(x=300, y =150)

#bottom box
Frame_image = PhotoImage(file = "./weather_icons/Copy of box.png")
frame_image = Label(image = Frame_image)
frame_image.pack(padx= 5, pady =5, side = BOTTOM)


#time
name = Label(window,font = ("arial", 15, "bold"))
name.place(x=30, y =100)
clock = Label(window, font =("Helvetica", 20))
clock.place(x=30, y =130)


label1 = Label(window,text = "WIND", font = ("Helvetica",15,'bold'), fg ="white", bg = "#1ab5ef")
label1.place(x=100, y = 400)

label2 = Label(window,text = "HUMIDITY", font = ("Helvetica",15,'bold'), fg ="white", bg = "#1ab5ef")
label2.place(x=250, y = 400)

label3 = Label(window,text = "DESCRIPTION", font = ("Helvetica",15,'bold'), fg ="white", bg = "#1ab5ef")
label3.place(x=450, y = 400)

label4 = Label(window,text = "PRESSURE", font = ("Helvetica",15,'bold'), fg ="white", bg = "#1ab5ef")
label4.place(x=700, y = 400)




t =Label(font=("arial",70,"bold"), fg = "#ee666d")
t.place(x =450, y = 100)
c = Label (font= ("arial", 15, 'bold'))
c.place(x=450, y = 250)

w = Label(text="...", font = ("arial", 15, 'bold'), bg = "#1ab5ef")
w.place(x=115, y= 430)
h = Label(text="...", font = ("arial", 15, 'bold'), bg = "#1ab5ef")
h.place(x=280, y= 430)
d = Label(text="...", font = ("arial", 15, 'bold'), bg = "#1ab5ef")
d.place(x=500, y= 430)
p = Label(text="...", font = ("arial", 15, 'bold'), bg = "#1ab5ef")
p.place(x=740, y= 430)

# Run the Tkinter event loop
window.mainloop()
