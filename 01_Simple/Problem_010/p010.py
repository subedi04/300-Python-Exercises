'''
Write A Python Program to get 6 subject marks from the user and calculate total and average of that marks. And display to user.
'''

def Enter_Marks():
    print("You must enter 6 marks")
    marks = []
    for i in range(0,6):
        num = float(input("Enter your mark number : "))
        marks.append(num)
    return marks

def Sum_Total(marks):
    total = 0
    for i in range(0,len(marks)):
        total += marks[i]
    return total

def Average(marks):
    return Sum_Total(marks)/len(marks)

if __name__=="__main__":
    marks = Enter_Marks()
    print("The sum is : ",Sum_Total(marks))
    print("The average is : ",Average(marks))