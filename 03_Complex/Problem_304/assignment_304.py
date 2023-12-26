import tkinter as tk

def display_substring():
    input_string = entry.get()
    start_index = int(start_entry.get())
    end_index = int(end_entry.get())

    try:
        result_string = input_string[start_index:end_index]
        result_label.config(text=f"Substring: {result_string}")
    except IndexError:
        result_label.config(text="Invalid indices. Please check the input.")

# Create the main window
window = tk.Tk()
window.title("Substring Extractor")

# Create and place widgets in the window
label = tk.Label(window, text="Enter a string:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

start_label = tk.Label(window, text="Start index:")
start_label.pack()

start_entry = tk.Entry(window)
start_entry.pack(pady=5)

end_label = tk.Label(window, text="End index:")
end_label.pack()

end_entry = tk.Entry(window)
end_entry.pack(pady=10)

extract_button = tk.Button(window, text="Extract Substring", command=display_substring)
extract_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main loop
window.mainloop()
