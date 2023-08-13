'''
Create a Desktop Python program to create a window and 
Insert some text to window. Also change label color, 
background color etc
'''

import tkinter as tk

def change_colors():
    label.config(fg=text_color.get(), bg=bg_color.get())


if __name__=="__main__":
    root = tk.Tk()
    root.title("Text and Color Changer")

    # Create a label
    label = tk.Label(root, text="Hello, I'm a label!")
    label.pack()

    # Create an entry for text color
    text_color_label = tk.Label(root, text="Text Color:")
    text_color_label.pack()

    text_color = tk.Entry(root)
    text_color.pack()

    # Create an entry for background color
    bg_color_label = tk.Label(root, text="Background Color:")
    bg_color_label.pack()

    bg_color = tk.Entry(root)
    bg_color.pack()

    # Create a button to change label colors
    change_colors_button = tk.Button(root, text="Change Colors", command=change_colors)
    change_colors_button.pack()

    root.mainloop()
