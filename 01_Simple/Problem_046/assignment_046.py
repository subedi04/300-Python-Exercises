'''
Write A Python Program To Get 5 Subject Marks, Store Them Into Array, 
And Also Get Student Name. Find Total And Average And Display Each Subjects Marks.

Expected result:
Hi username and your class is ---------
Your marks is ……
See your all subject marks
English = …
AI = …
Physics = …
Computer = …
Math= …
Your marks average is = ….
'''

import array as arr

def get_data():
    user = input("Enter your name :  ")
    a = arr.array('i',[])

    print("Enter subject marks in this order English, AI, Physics, Computer, Math")

    for i in range(5): #0, 1 , 2, 3, 4
        a.append(int(input("Enter subject marks : ")))
    return user,a

def Total(marks):
    total = 0
    for i in range(5): #0, 1 , 2, 3, 4
        total += marks[i] # a[0] => 50, a[1] =>60 
    return total

def Average(marks):
    return Total(marks)/len(marks)


def Display_Info(user,marks,total,average):
    print("\nHi, "+user+"!")
    print("Your marks is : "+str(total))
    print("Your average is : " + str(average))
    print("\nSee your all subject marks")
    print(">>> English = "+str(marks[0]))
    print(">>> AI = "+str(marks[1]))
    print(">>> Physics = "+str(marks[2]))
    print(">>> Computer = "+str(marks[3]))
    print(">>> Math = "+str(marks[4]))

if __name__=="__main__":
    user,marks = get_data()
    total = Total(marks)
    average = Average(marks)
    Display_Info(user,marks,total,average)



