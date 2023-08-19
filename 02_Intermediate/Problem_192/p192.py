'''
Write a Desktop Python program to get 
a year from user to check it is leap 
year or not.
'''


from tkinter import * 
win = Tk()
win.title("Leap Year")
win.geometry("500x500")

def get_value():
    year = int(e.get())
    if year%4 == 0:
        t = str(year)+" is the leap year"
        Label(win, text = t).pack()
    else:
        t = str(year)+" is not leap year"
        Label(win, text = t).pack()
   
   
Label(win, text="Enter a year").pack()
e = Entry(win, width=30)
e.pack()


Button(win, text="Check Year", command=get_value).pack()
win.mainloop()

