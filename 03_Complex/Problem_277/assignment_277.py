import tkinter as tk
from tkinter import ttk

def calculate_acceleration():
    try:
        velocity = float(velocity_entry.get())
        time = float(time_entry.get())
        acceleration = velocity / time
        result_label.config(text=f"Acceleration: {acceleration:.2f} m/s²")
    except ValueError:
        result_label.config(text="Please enter valid numerical values.")

# Create the main window
app = tk.Tk()
app.title("Acceleration Calculator")

# Create and place themed widgets
style = ttk.Style()
style.theme_use("clam")  # You can change the theme as needed

frame = ttk.Frame(app, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

velocity_label = ttk.Label(frame, text="Enter Velocity (m/s): ")
velocity_label.grid(column=0, row=0, pady=10, sticky=tk.W)

velocity_entry = ttk.Entry(frame)
velocity_entry.grid(column=1, row=0, pady=10, sticky=tk.W)

time_label = ttk.Label(frame, text="Enter Time (s):")
time_label.grid(column=0, row=1, pady=10, sticky=tk.W)

time_entry = ttk.Entry(frame)
time_entry.grid(column=1, row=1, pady=10, sticky=tk.W)

calculate_button = ttk.Button(frame, text="Calculate", command=calculate_acceleration)
calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=3, columnspan=2, pady=10)

# Start the main loop
app.mainloop()
