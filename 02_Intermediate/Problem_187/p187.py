'''
Create a Desktop Python Program to insert Image in Window.
'''

from tkinter import * 

if __name__=="__main__":
	win = Tk()
	win.title("Image as backgorund.,,")
	# win.geometry("300x300")
	img = PhotoImage(file="pic.png")
	l = Label(win, image=img)
	l.pack()
	win.mainloop()

