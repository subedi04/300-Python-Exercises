import tkinter as tk

def get_odd_characters():
    input_text = entry.get()
    odd_characters = input_text[1::2]  # Get characters at odd index numbers
    result_label.config(text=f"Characters at odd index: {odd_characters}")

# Create the main window
window = tk.Tk()
window.title("Odd Index Characters Extractor")

# Create and place widgets in the window
label = tk.Label(window, text="Enter a string:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

extract_button = tk.Button(window, text="Extract Odd Characters", command=get_odd_characters)
extract_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main loop
window.mainloop()
