from tkinter import *

root = Tk()
root.geometry("600x250")

def get_value():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    if num1 > num2:
        Label(root, text ="Num1 is greater than num2").pack()
    elif num2 > num1:
        Label(root, text ="Num2 is greater than num1").pack()
    else:
        Label(root, text ="Numbers are equal to each other...").pack()

entry1 = Entry(root, width="40")
entry1.pack(pady=10)

entry2 = Entry(root, width="40")
entry2.pack()

btn = Button(root, text="Enter", command=get_value)
btn.pack()
root.mainloop()