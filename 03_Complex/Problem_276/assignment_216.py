import tkinter as tk

def calculate_increment():
    try:
        user_number = int(entry.get())
        auto_increment = user_number // 2
        result_label.config(text=f"Result: {user_number + auto_increment}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main window
app = tk.Tk()
app.title("Auto Increment Calculator")

# Create and place widgets
label = tk.Label(app, text="Enter a number: ")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

calculate_button = tk.Button(app, text="Calculate", command=calculate_increment)
calculate_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Start the main loop
app.mainloop()
