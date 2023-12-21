from tkinter import *

root = Tk()
root.geometry("600x350")

def get_value():
    num = int(entry.get())
    for i in range(1, 11):
        # 1 * 2 = 2
        # 2 * 2 = 4
        table = str(i)+" * "+str(num)+" = "+str(i*num)
        Label(root, text=table).pack()


entry = Entry(root, width="40")
entry.pack(pady=10)

btn = Button(root, text="Enter", command=get_value)
btn.pack()
root.mainloop()