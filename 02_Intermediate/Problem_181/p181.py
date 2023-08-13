'''
Create a Desktop Python program to create a window as resizable.
'''

from tkinter import * 

if __name__=="__main__":
    root = Tk()
    root.title("Window Title Example...")
    root.geometry("500x500")
    root.resizable(True, False)
    root.mainloop()