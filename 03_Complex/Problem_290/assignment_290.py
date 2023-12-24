import tkinter as tk
from tkinter import simpledialog, messagebox

def get_name_and_age():
    try:
        name = simpledialog.askstring("Enter Name", "Please enter your name:")
        if name:
            age = simpledialog.askinteger("Enter Age", "Please enter your age:")
            if age is not None:
                message = f"Hi {name}! Your age is {age}."
                messagebox.showinfo("Greeting", message)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid information.")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("User Information App")

    # Create and configure a button
    button = tk.Button(root, text="Get Information", command=get_name_and_age)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
