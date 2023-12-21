from cProfile import label
from tkinter import *

root = Tk()
root.geometry("600x250")

def get_value():
    user_st = entry.get()
    total_char = len(user_st)
    sp = 0
    for i in user_st:
        if i.isspace():
            sp += 1
    total_words = sp + 1
    Label(root, text="Total Char = "+str(total_char)).pack()
    Label(root, text="Total Words = "+str(total_words)).pack()
    Label(root, text="Total Spaces = "+str(sp)).pack()


entry = Entry(root, width="40")
entry.pack(pady=10)

btn = Button(root, text="Enter", command=get_value)
btn.pack()
root.mainloop()