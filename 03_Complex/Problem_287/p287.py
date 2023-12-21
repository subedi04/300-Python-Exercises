from email import message
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x350")
messagebox.askokcancel("Here is title as cencel","Are you want to cencel?")
messagebox.askquestion("question","do you need it?")
messagebox.askretrycancel("title","message")
messagebox.askyesno("YESNO TITLE","Do you want to save this file?")
messagebox.askyesnocancel("Title","Do you want to exit program")
root.mainloop()