'''
Create a Desktop Python program to create 
a window and provide title with icon.
'''

import tkinter as tk

root = tk.Tk()
root.title("Window with Title and Icon")

# Set the window icon (provide the path to your icon file)
icon_path = "path/to/your/icon.ico"
root.iconbitmap(icon_path)

# Create a label
label = tk.Label(root, text="Hello, I'm a label!")
label.pack()

root.mainloop()
