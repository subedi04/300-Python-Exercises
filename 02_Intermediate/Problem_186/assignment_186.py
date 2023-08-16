'''
Write a Desktop Python program to create a Checkboxes to 
change background color, cursor, font, fg, border etc.
'''


import tkinter as tk
from tkinter import font

def update_label():
    # Background color
    if bg_var.get():
        lbl.config(bg="lightblue")
    else:
        lbl.config(bg="SystemButtonFace")
    
    # Cursor
    if cursor_var.get():
        lbl.config(cursor="circle")
    else:
        lbl.config(cursor="arrow")

    # Font
    if font_var.get():
        lbl.config(font=custom_font)
    else:
        lbl.config(font=default_font)

    # Foreground color
    if fg_var.get():
        lbl.config(fg="red")
    else:
        lbl.config(fg="black")
    
    # Border
    if border_var.get():
        lbl.config(relief="ridge", bd=5)
    else:
        lbl.config(relief="flat", bd=1)


if __name__=="__main__":
	root = tk.Tk()
	root.title("Checkbox UI Customizer")

	# Variables to track checkbox states
	bg_var = tk.BooleanVar()
	cursor_var = tk.BooleanVar()
	font_var = tk.BooleanVar()
	fg_var = tk.BooleanVar()
	border_var = tk.BooleanVar()

	# Fonts
	default_font = font.nametofont("TkDefaultFont")
	custom_font = font.Font(family="Arial", size=12, weight="bold")

	# Label to be customized
	lbl = tk.Label(root, text="Customize me using checkboxes!", pady=20, padx=20)
	lbl.pack(pady=20)

	# Checkboxes
	bg_cb = tk.Checkbutton(root, text="Change Background", variable=bg_var, command=update_label)
	bg_cb.pack(anchor="w", padx=20)

	cursor_cb = tk.Checkbutton(root, text="Change Cursor", variable=cursor_var, command=update_label)
	cursor_cb.pack(anchor="w", padx=20)

	font_cb = tk.Checkbutton(root, text="Change Font", variable=font_var, command=update_label)
	font_cb.pack(anchor="w", padx=20)

	fg_cb = tk.Checkbutton(root, text="Change Foreground", variable=fg_var, command=update_label)
	fg_cb.pack(anchor="w", padx=20)

	border_cb = tk.Checkbutton(root, text="Change Border", variable=border_var, command=update_label)
	border_cb.pack(anchor="w", padx=20)

	root.mainloop()


