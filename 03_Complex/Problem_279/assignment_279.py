import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        numbers = [int(num_entry.get()) for num_entry in entry_list]
        result = sum(num for num in numbers if 5 < num < 10)
        messagebox.showinfo("Result", f"Sum of numbers between 5 and 10: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main application window
app = tk.Tk()
app.title("Number Sum Calculator")

# Create and place Entry widgets for user input
entry_list = []
for i in range(5):
    entry_label = tk.Label(app, text=f"Number {i + 1}:")
    entry_label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

    entry = tk.Entry(app)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entry_list.append(entry)

# Create and place the "Calculate" button
calculate_button = tk.Button(app, text="Calculate Sum", command=calculate_sum)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
app.mainloop()
