from io import BytesIO

from PIL import Image, ImageTk, ImageFilter
import requests
import json
import tkinter as tk
from data.Data import Data


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







window = tk.Tk()

# Set the default window size
default_width = 1000
default_height = 600
window.geometry(f"{default_width}x{default_height}")

# Load the image
image = Image.open("./background_pictures/cloud-blue-sky.jpg")  # Replace "background_image.jpg" with your image file

# Resize the image to fit the window size
resized_image = image.resize((default_width, default_height), Image.ANTIALIAS)

# Apply a blur filter to the image
blurred_image = resized_image.filter(ImageFilter.BLUR)

# Convert the blurred image to Tkinter-compatible format
photo = ImageTk.PhotoImage(blurred_image)

# Create a Label widget with the blurred image
label = tk.Label(window, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the sections
frame = tk.Frame(window, padx=10, pady=10)
frame.pack(side=tk.TOP)

# City Name Section
city_label = tk.Label(frame, text="City Name", font=("Arial", 16))
city_label.pack(anchor=tk.W)

# Temperature Section
temp_label = tk.Label(frame, text="Temperature: ", font=("Arial", 14))
temp_label.pack(anchor=tk.W)

# Weather Condition Section
condition_label = tk.Label(frame, text="Weather Condition: ", font=("Arial", 14))
condition_label.pack(anchor=tk.W)

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