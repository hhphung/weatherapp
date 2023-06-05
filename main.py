from io import BytesIO

from PIL import Image, ImageTk
import requests
import json
import tkinter as tk


def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def display_weather(data):
    location = data['name']
    temperature = data['main']['temp']
    weather_condition = data['weather'][0]['description']
    weather_icon_id = data['weather'][0]['icon']

    root = tk.Tk()
    root.title("Weather App")

    weather_label = tk.Label(root,
                             text=f"Weather in {location}:\nTemperature: {temperature} K\nCondition: {weather_condition}",
                             padx=10, pady=10)
    weather_label.pack()

    # Load weather icon from URL
    weather_icon_url = f"http://openweathermap.org/img/wn/{weather_icon_id}.png"
    response = requests.get(weather_icon_url)
    image_data = response.content
    photo = ImageTk.PhotoImage(Image.open(BytesIO(image_data)))

    # Display weather icon using Label widget
    weather_icon_label = tk.Label(root, image=photo)
    weather_icon_label.pack()

    root.mainloop()


if __name__ == "__main__":
    api_key = "00beef8fc9c995b42a522b5f790ee829"
    location = "New York"

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)












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