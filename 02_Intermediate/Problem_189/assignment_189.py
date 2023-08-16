'''
Write a Desktop Python program to get 
a string from user to change uppercase 
if user string is in lowercase.
'''

import tkinter as tk
from tkinter import simpledialog, messagebox

def check_and_convert():
    user_input = simpledialog.askstring("Input", "Enter a string:")
    
    if user_input.islower():
        messagebox.showinfo("Result", user_input.upper())
    else:
        messagebox.showinfo("Result", "String is not in lowercase or contains mixed cases")

if __name__=="__main__":
	root = tk.Tk()
	root.title("Lowercase to Uppercase Converter")

	btn = tk.Button(root, text="Enter a string", command=check_and_convert)
	btn.pack(pady=50)

	root.mainloop()

