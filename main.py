from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import requests
import json
import tkinter as tk
import random
import pytz

window = tk.Tk()
api_key = "00beef8fc9c995b42a522b5f790ee829"
location = "Florida"
# Set the default window size
default_width = 900
default_height = 500
window.geometry(f"{default_width}x{default_height}+300+200")
window.resizable(False,False)

# Load the background image
background_image = Image.open("./background_pictures/background.jpg")

# Resize the background image to fit the window size
resized_background = background_image.resize((default_width, default_height), Image.ANTIALIAS)

# Apply a blur filter to the background image
blurred_background = resized_background.filter(ImageFilter.BLUR)

# Convert the blurred background image to Tkinter-compatible format
background_photo = ImageTk.PhotoImage(blurred_background)

# Load the picture to be displayed on the left
weather_condition = Image.open("./weather_icons/cloudy.png")

# Resize the picture image to fit within the frame
picture_width = 100
picture_height = default_height - 400
resized_picture = weather_condition.resize((picture_width, picture_height), Image.ANTIALIAS)

# Convert the resized picture image to Tkinter-compatible format
picture_photo = ImageTk.PhotoImage(resized_picture)




def search():
    text = textField.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={text}&APPID={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)


search_image = PhotoImage(file="./weather_icons/search_box.png")
search_image = search_image.subsample(2)
search_box = Label(image=search_image)
search_box.place(x=20, y=20)

textField = Entry(window, justify="center", width=17, font=("poppins", 20, "bold"), bg="#595959", border=0, fg="white")
textField.place(x=30, y=30)
textField.focus()

search_icon = PhotoImage(file="./weather_icons/search_Icon.png")
search_icon = search_icon.subsample(22)

my_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#595959", command=search())
my_icon.place(x=250, y=22)


#logo
Logo_image = PhotoImage(file = "./weather_icons/cloudy.png")
Logo_image = Logo_image.subsample(4)
logo = Label(image = Logo_image)
logo.place(x=350, y =150)

#bottom box
Frame_image = PhotoImage(file = "./weather_icons/bottom_bar.png")
frame_image = Label(image = Frame_image)
frame_image.pack(padx= 5, pady =5, side = BOTTOM)


label1 = Label(window,text = "WIND", font = ("Helvetica",15,'bold'), fg ="white", bg = "#1ab5ef")
label1.place(x=100, y = 400)

label2 = Label(window,text = "HUMIDITY", font = ("Helvetica",15,'bold'), fg ="white", bg = "#1ab5ef")
label2.place(x=250, y = 400)

label3 = Label(window,text = "DESCRIPTION", font = ("Helvetica",15,'bold'), fg ="white", bg = "#1ab5ef")
label3.place(x=450, y = 400)

label4 = Label(window,text = "PRESSURE", font = ("Helvetica",15,'bold'), fg ="white", bg = "#1ab5ef")
label4.place(x=700, y = 400)




t =Label(font=("arial",70,"bold"), fg = "#ee666d")
t.place(x =400, y = 100)
c = Label (font= ("arial", 15, 'bold'))
c.place(x=400, y = 250)

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
