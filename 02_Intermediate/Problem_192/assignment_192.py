'''
Write a Python program to get a year from user
to check it is leap year or not using OOP
'''

import tkinter as tk
from tkinter import messagebox

class LeapYearChecker:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        # If the year is divisible by 4
        if self.year % 4 == 0:
            # If the year is divisible by 100
            if self.year % 100 == 0:
                # If the year is divisible by 400, then it's a leap year
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

def check_year():
    year = year_entry.get()
    
    if not year.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a valid year!")
        return

    year = int(year)
    checker = LeapYearChecker(year)
    
    if checker.is_leap_year():
        messagebox.showinfo("Result", f"{year} is a Leap Year!")
    else:
        messagebox.showwarning("Result", f"{year} is not a Leap Year!")


if __name__=="__main__":
	root = tk.Tk()
	root.title("Leap Year Checker")

	# Create and place the widgets
	label = tk.Label(root, text="Enter a year:")
	label.pack(pady=10)

	year_entry = tk.Entry(root, width=40)
	year_entry.pack(pady=10)

	button = tk.Button(root, text="Check", command=check_year)
	button.pack(pady=20)

	root.mainloop()

