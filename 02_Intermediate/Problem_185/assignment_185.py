'''
Create a Desktop Python Program to insert a Image as button with text in Window.
'''


import tkinter as tk
from PIL import Image, ImageTk

def on_button_click():
    print("Button clicked!")


if __name__=="__main__":
	root = tk.Tk()
	root.title("Image Button with Text")

	# Load the image
	image_path = "image.png"
	image = Image.open(image_path)
	photo = ImageTk.PhotoImage(image)

	# Create the button with image and text
	button = tk.Button(root, image=photo, text="Click Me!", compound=tk.TOP, command=on_button_click)
	button.pack(pady=20)

	# Run the application
	root.mainloop()

