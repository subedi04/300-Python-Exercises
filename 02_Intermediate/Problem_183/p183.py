'''
Create a Desktop Python Program to insert a 
Button in Window. When click on that button 
a function should run
'''

from tkinter import * 

if __name__=="__main__":
    root = Tk()
    root.title("Button clicking...")
    root.geometry("300x300")
    def myfunc():
        print("Button is clicked.....")

    btn = Button(root, text="Click me", command=myfunc)
    btn.pack()
    root.mainloop()