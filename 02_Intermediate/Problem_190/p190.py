'''
Write a Desktop Python program to get 
a character from user to check whether 
it is vowel or not. 
'''

from tkinter import * 
win = Tk()
win.title("Check Vowel Char")
win.geometry("500x500")

def get_value():
    char = e.get()
    # a e i o u 
    if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U':
        Label(win, text = "This is the Vowel char").pack()
    else:
        Label(win, text = "This is not a vowel").pack()
   
   
if __name__=="__main__":
	Label(win, text="Enter a character").pack()
	e = Entry(win, width=30)
	e.pack()
	Button(win, text="Get Answer", command=get_value).pack()
	win.mainloop()

