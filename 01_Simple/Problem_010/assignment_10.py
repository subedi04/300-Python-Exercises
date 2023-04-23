'''
Write A Python Program to get 6 subject marks from the user and calculate total, 
average and percentage of that marks. And display to user.
'''

def Enter_Marks():
    print("You must enter 6 marks")
    marks = []
    for i in range(0,6):
        num = float(input("Enter your mark number : "))
        marks.append(num)
    return marks

def Sum_Total(marks):
    return sum([mark for mark in marks])

def Average(marks):
    return Sum_Total(marks)/len(marks)

def Percent_Marks(marks):
    print("\nPercentage of the numbers")
    total = Sum_Total(marks)
    for i in range(0,len(marks)):
        print(marks[i]," is the ",round((marks[i]*100)/total,2),"%\tof total.")




if __name__=="__main__":
    marks = Enter_Marks()
    print("\n")
    print("The sum is : ",Sum_Total(marks))
    print("The average is : ",Average(marks))
    Percent_Marks(marks)
