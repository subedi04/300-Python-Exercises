'''
Write a Python Program To find array size in bytes.
'''

import tkinter as tk
from tkinter import messagebox
import sys

class ArraySizeChecker:
    def __init__(self, array):
        self.array = array

    def get_size_in_bytes(self):
        return sys.getsizeof(self.array)

def check_array_size():
    input_data = array_entry.get()
    try:
        array = [int(item.strip()) for item in input_data.split(',')]
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a comma-separated list of numbers!")
        return

    checker = ArraySizeChecker(array)
    size = checker.get_size_in_bytes()
    messagebox.showinfo("Result", f"Size of the array is {size} bytes.")

if __name__=="__main__":
	root = tk.Tk()
	root.title("Array Size Checker")

	# Create and place the widgets
	label = tk.Label(root, text="Enter a comma-separated list of numbers:")
	label.pack(pady=10)

	array_entry = tk.Entry(root, width=50)
	array_entry.pack(pady=10)

	button = tk.Button(root, text="Check Size", command=check_array_size)
	button.pack(pady=20)

	root.mainloop()

