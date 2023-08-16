'''
Write a Desktop Python program to get first 
and last name from user to display full name 
to user.
'''

from tkinter import * 

win = Tk()
win.title("First and Last name")
win.geometry("500x500")

def get_value():
    f_name = e1.get()
    l_name = e2.get()
    full_name = f_name +" "+ l_name
    Label(win, text=full_name).pack()

if __name__=="__main__":
	l1 = Label(win, text="Enter first name").pack()
	e1 = Entry(win, width=30)
	e1.pack()

	l2 = Label(win, text="Enter Last name").pack()
	e2 = Entry(win, width=30)
	e2.pack()

	Button(win, text="Get Full Name", command=get_value).pack()
	win.mainloop()

