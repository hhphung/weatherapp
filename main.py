from io import BytesIO
from PIL import Image, ImageTk, ImageFilter
import requests
import json
import tkinter as tk
import random
from data.Data import Data

window = tk.Tk()

# Set the default window size
default_width = 1000
default_height = 500
window.geometry(f"{default_width}x{default_height}")

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


def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    a = Data(data)
    return a


def display_weather(data):
    location = data.name
    temperature = data.temp_in_F()
    weather_condition = data.weather_desc

    # Create a Label widget with the blurred background image
    background_label = tk.Label(window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame for the sections
    frame = tk.Frame(window, padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create a Label widget for the picture on the left
    picture_label = tk.Label(frame, image=picture_photo)
    picture_label.pack(side=tk.LEFT)

    # City Name Section
    city_label = tk.Label(frame, text=location, font=("Arial", 16))
    city_label.pack(anchor=tk.W)

    # Temperature Section
    temp_label = tk.Label(frame, text=str(temperature) + " F", font=("Arial", 50))
    temp_label.pack(anchor=tk.W)

    # Create a frame for the additional weather information
    frame_bottom = tk.Frame(window, padx=10, pady=10)
    frame_bottom.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    # Wind Section
    wind_label = tk.Label(frame_bottom, text=f"Wind: {random.randint(0, 50)} mph", font=("Arial", 14))
    wind_label.pack(side=tk.LEFT, padx=10)

    # Humidity Section
    humidity_label = tk.Label(frame_bottom, text=f"Humidity: {random.randint(0, 100)}%", font=("Arial", 14))
    humidity_label.pack(side=tk.LEFT, padx=10)

    # Description Section
    description_label = tk.Label(frame_bottom, text="Description: Some random description", font=("Arial", 14))
    description_label.pack(side=tk.LEFT, padx=10)

    # Pressure Section
    pressure_label = tk.Label(frame_bottom, text=f"Pressure: {random.randint(900, 1100)} hPa", font=("Arial", 14))
    pressure_label.pack(side=tk.LEFT, padx=10)


api_key = "00beef8fc9c995b42a522b5f790ee829"
location = "Florida"
data = get_weather(api_key, location)
display_weather(data)

# Run the Tkinter event loop
window.mainloop()