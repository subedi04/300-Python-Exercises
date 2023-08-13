'''
Create a Desktop Python Program to insert 
a Button in Window. A message box should be 
display when user click on the button.
'''

import tkinter as tk
from tkinter import messagebox

def show_message_box():
    messagebox.showinfo("Message", "Button Clicked!")

if __name__=="__main__":
    root = tk.Tk()
    root.title("Message Box Program")

    # Create a button to display message box
    button = tk.Button(root, text="Click Me", command=show_message_box)
    button.pack()

    root.mainloop()
