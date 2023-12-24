from tkinter import *
from tkinter import simpledialog

root = Tk()

age = simpledialog.askinteger("Input","Enter your age", parent=root)
name = simpledialog.askstring("Input","Enter your name", parent=root)
print(f"Hi {name}! your age is "+str(age))
root.mainloop()
