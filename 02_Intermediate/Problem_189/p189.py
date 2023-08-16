'''
Write a Desktop Python program to get 
two number from user to display their 
reminder after division.
'''

from tkinter import * 
win = Tk()
win.title("Two Number Reminder")
win.geometry("500x500")

def get_value():
    n1 = int(e1.get())
    n2 = int(e2.get())
    ans = n1 % n2
    Label(win, text=ans).pack()
    
if __name__=="__main__":
	Label(win, text="Enter first number").pack()
	e1 = Entry(win, width=30)
	e1.pack()
	Label(win, text="Enter 2nd number").pack()
	e2 = Entry(win, width=30)
	e2.pack()

	Button(win, text="Get Answer", command=get_value).pack()
	win.mainloop()

