'''
Write a Desktop Python program to get a string from user to reverse.
'''

import tkinter as tk
from tkinter import simpledialog, messagebox

def reverse_string():
	user_input = simpledialog.askstring("Input", "Enter a string:")
	reversed_str = user_input[::-1]
  messagebox.showinfo("Result", f"Reversed string: {reversed_str}")


if __name__=="__main__":
	root = tk.Tk()
	root.title("String Reverser")

	btn = tk.Button(root, text="Enter a string to reverse", command=reverse_string)
	btn.pack(pady=50)

	root.mainloop()

