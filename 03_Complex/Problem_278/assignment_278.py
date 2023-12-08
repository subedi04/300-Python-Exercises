import tkinter as tk
from tkinter import messagebox

def calculate_force():
    try:
        mass = float(entry_mass.get())
        acceleration = float(entry_acceleration.get())

        force = mass * acceleration

        result_label.config(text=f"Force: {force} Newtons")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for Mass and Acceleration.")



app = tk.Tk()
app.title("Force Calculator")

# Labels
label_mass = tk.Label(app, text="Enter Mass (kg):")
label_acceleration = tk.Label(app, text="Enter Acceleration (m/s^2):")
result_label = tk.Label(app, text="Force:")

# Entry widgets
entry_mass = tk.Entry(app)
entry_acceleration = tk.Entry(app)

# Button
calculate_button = tk.Button(app, text="Calculate Force", command=calculate_force)

# Layout
label_mass.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_mass.grid(row=0, column=1, padx=10, pady=10)
label_acceleration.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_acceleration.grid(row=1, column=1, padx=10, pady=10)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()
