'''
Create a Desktop Python program to create a window and Insert a Button.
'''

import tkinter as tk

def button_clicked():
    label.config(text="Button Clicked!")


if __name__=="__main__":
    root = tk.Tk()
    root.title("Window with Button")

    # Create a button
    button = tk.Button(root, text="Click Me", command=button_clicked)
    button.pack()

    # Create a label
    label = tk.Label(root, text="")
    label.pack()

    root.mainloop()
