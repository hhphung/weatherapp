import tkinter as tk
from PIL import Image, ImageTk, ImageFilter

# Create the main window
window = tk.Tk()

# Load the image
image = Image.open("./background_pictures/cloud-blue-sky.jpg")  # Replace "background_image.jpg" with your image file

# Resize the image to fit the window size
image = image.resize((800, 600), Image.ANTIALIAS)  # Adjust the width and height as desired

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.BLUR)

# Convert the blurred image to Tkinter-compatible format
photo = ImageTk.PhotoImage(blurred_image)

# Create a Label widget with the blurred image
label = tk.Label(window, image=photo)
label.pack()

# Create a button
button = tk.Button(window, text="Click Me")

# Position the button in the bottom right corner
button.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-10, y=-10)

# Run the Tkinter event loop
window.mainloop()