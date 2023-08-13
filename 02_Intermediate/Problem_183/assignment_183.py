'''
Create a Desktop Python Program to insert a Button in Window. 
When click on the button, it take two number from user to add 
both number in console.
'''

import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__=="__main__":
    root = tk.Tk()
    root.title("Addition Program")

    # Create entry fields for numbers
    entry_num1 = tk.Entry(root)
    entry_num1.pack()

    entry_num2 = tk.Entry(root)
    entry_num2.pack()

    add_button = tk.Button(root, text="Add Numbers", command=add_numbers)
    add_button.pack()

    root.mainloop()
