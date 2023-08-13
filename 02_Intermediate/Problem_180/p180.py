'''
Create a Desktop Python program to create 
a window and Insert some text to window
'''

from tkinter import * 

if __name__=="__main__":
    root = Tk()
    root.title("Window Title Example...")
    text = Label(root, text="How are you")
    text.pack()
    text1 = Label(root, text="Another text....")
    text1.pack()
    root.mainloop()