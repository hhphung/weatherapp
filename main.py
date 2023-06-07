from io import BytesIO
from PIL import Image, ImageTk, ImageFilter
import requests
import json
import tkinter as tk
import random

window = tk.Tk()

# Set the default window size
default_width = 1000
default_height = 500
window.geometry(f"{default_width}x{default_height}")

# Load the image
image = Image.open("./background_pictures/cloud-blue-sky.jpg")  # Replace "background_image.jpg" with your image file

# Resize the image to fit the window size
resized_image = image.resize((default_width, default_height), Image.ANTIALIAS)

# Apply a blur filter to the image
blurred_image = resized_image.filter(ImageFilter.BLUR)

# Convert the blurred image to Tkinter-compatible format
photo = ImageTk.PhotoImage(blurred_image)


class Data:
    def __init__(self, weather_data):
        self.name = weather_data["name"]
        self.temp_in_K = weather_data["main"]["temp"]
        self.weather_desc = weather_data["weather"][0]["description"]

    def temp_in_F(self):
        return (self.temp_in_K - 273.15) * 9/5 + 32


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

    # Create a Label widget with the blurred image
    label = tk.Label(window, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame for the sections
    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack(side=tk.TOP)

    # City Name Section
    city_label = tk.Label(frame, text=location, font=("Arial", 16))
    city_label.pack(anchor=tk.W)

    # Temperature Section
    temp_label = tk.Label(frame, text=str(temperature) + " F", font=("Arial", 50))
    temp_label.pack(anchor=tk.W)

    # Weather Condition Section
    condition_label = tk.Label(frame, text=weather_condition, font=("Arial", 14))
    condition_label.pack(anchor=tk.W)

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
















""" 
# Create the main window
window = tk.Tk()

# Set the window size
window.geometry("800x600")

# Load the image
image = Image.open("./background_pictures/cloud-blue-sky.jpg")  # Replace "background_image.jpg" with your image file

# Resize the image to fit the window size
image = image.resize((800, 600), Image.ANTIALIAS)  # Adjust the width and height as desired

# Convert the image to Tkinter-compatible format
photo = ImageTk.PhotoImage(image)

# Create a Label widget with the image
label = tk.Label(window, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to display a black screen
def display_black_screen():
    label.configure(image='')
    window.configure(bg="black")

# Create a button
button = tk.Button(window, text="Click Me", command=display_black_screen)

# Position the button in the bottom right corner
button.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-10, y=-10)

# Run the Tkinter event loop
window.mainloop()


"""