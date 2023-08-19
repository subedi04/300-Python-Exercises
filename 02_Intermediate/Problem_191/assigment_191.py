'''
Write a Desktop Python program to get a string from 
user which contain alpha at starting and ending position.
'''

import tkinter as tk
from tkinter import messagebox

def check_string():
	user_input = entry.get()
    
	if user_input and user_input[0].isalpha() and user_input[-1].isalpha():
  	messagebox.showinfo("Result", "Valid string!")
  else:
  	messagebox.showwarning("Result", "Invalid string! The string should start and end with an alphabetical character.")

if __name__=="__main__":
	root = tk.Tk()
	root.title("String Checker")

	# Create and place the widgets
	label = tk.Label(root, text="Enter a string:")
	label.pack(pady=10)

	entry = tk.Entry(root, width=40)
	entry.pack(pady=10)

	button = tk.Button(root, text="Check", command=check_string)
	button.pack(pady=20)

	root.mainloop()

