import tkinter as tk
from tkinter import simpledialog, messagebox

def get_integer():
    try:
        user_input = simpledialog.askinteger("Enter Integer", "Please enter an integer:")
        if user_input is not None:
            square = user_input ** 2
            messagebox.showinfo("Result", f"The square of {user_input} is {square}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Integer Square Calculator")

    # Create and configure a button
    button = tk.Button(root, text="Get Square", command=get_integer)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
