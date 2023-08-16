'''
Create a Desktop Python Program to insert Image 
in Window when a user click on button.
'''

import tkinter as tk
from PIL import Image, ImageTk

def show_image():
    # Load the image
    image_path = "image.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Display the image
    img_label = tk.Label(root, image=photo)
    img_label.image = photo  # keep a reference to avoid garbage collection
    img_label.pack(pady=20)

if __name__=="__main__":
	# Create the main window
	root = tk.Tk()
	root.title("Display Image on Button Click")

	# Create the button
	button = tk.Button(root, text="Show Image", command=show_image)
	button.pack(pady=20)

	# Run the application
	root.mainloop()


