import tkinter as tk
from tkinter import messagebox
import re

def check_password():
    password = entry.get()

    # Check if the password contains at least one alphanumeric character and one special character
    if re.match(r'^(?=.*[a-zA-Z0-9])(?=.*[!@#$%^&*()_+])', password):
        messagebox.showinfo("Password Check", "Password is valid!")
    else:
        messagebox.showerror("Password Check", "Password must contain at least one alphanumeric character and one special character.")

# Create the main window
window = tk.Tk()
window.title("Password Checker")

# Create and place widgets in the window
label = tk.Label(window, text="Enter a password:")
label.pack(pady=10)

entry = tk.Entry(window, show="*")
entry.pack(pady=10)

check_button = tk.Button(window, text="Check Password", command=check_password)
check_button.pack(pady=10)

# Start the main loop
window.mainloop()
