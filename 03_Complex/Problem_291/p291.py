from tkinter import *

root = Tk()

lst = Listbox(root, bd=10, fg="yellow", bg="black", cursor="cross")
lst.insert(0,"Python")
lst.insert(1,"C++")
lst.insert(2,"HTML")

lst.pack()
"""
"arrow"
"circle"
"clock"
"cross"
"dotbox"
"exchange"
"fleur"
"heart"
"heart"
"man"
"mouse"
"pirate"
"plus"
"""
root.mainloop()
