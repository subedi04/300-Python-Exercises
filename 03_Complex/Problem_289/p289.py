from tkinter import *
from tkinter import simpledialog

root = Tk()

number = simpledialog.askinteger("Input","Enter a number : ", parent=root)
print("Square of your entered number is "+str(number*number))
root.mainloop()
