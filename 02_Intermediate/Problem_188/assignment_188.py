'''
Write a Desktop Python program to get first 
and last name from user to display full name 
to user.
'''

import tkinter as tk
from tkinter import messagebox

def calculate_cube():
    try:
        # Get the number from the entry widget
        num = float(entry.get())
        
        # Calculate the cube of the number
        cube = num ** 3
        
        # Display the result
        result_label.config(text=f"Cube of {num} is: {cube}")
    except ValueError:
        # Show an error message if the input is not a valid number
        messagebox.showerror("Error", "Please enter a valid number!")

if __name__=="__main__":
	# Create the main window
	root = tk.Tk()
	root.title("Cube Calculator")

	# Label to prompt the user
	prompt_label = tk.Label(root, text="Enter a number:")
	prompt_label.pack(pady=10)

	# Entry widget for user input
	entry = tk.Entry(root)
	entry.pack(pady=10)

	# Button to trigger the calculation
	calc_button = tk.Button(root, text="Calculate Cube", command=calculate_cube)
	calc_button.pack(pady=10)

	# Label to display the result
	result_label = tk.Label(root, text="")
	result_label.pack(pady=10)

	# Run the application
	root.mainloop()

