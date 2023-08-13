'''
Create a Desktop Python program to provide width and height to window.
'''

import tkinter as tk

def set_window_size():
    width = int(width_entry.get())
    height = int(height_entry.get())
    root.geometry(f"{width}x{height}")

if __name__=="__main__":
    root = tk.Tk()
    root.title("Window Size Setter")

    # Create labels and entry fields for width and height
    width_label = tk.Label(root, text="Width:")
    width_label.pack()

    width_entry = tk.Entry(root)
    width_entry.pack()

    height_label = tk.Label(root, text="Height:")
    height_label.pack()

    height_entry = tk.Entry(root)
    height_entry.pack()

    # Create a button to set the window size
    set_size_button = tk.Button(root, text="Set Size", command=set_window_size)
    set_size_button.pack()

    root.mainloop()
