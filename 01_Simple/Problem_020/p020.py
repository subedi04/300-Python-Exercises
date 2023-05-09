'''
Write A Python Program To Get 5 Number From 
User In Array And Sum All Number And Display
'''

# get 5 number from the user
# store in the array and display 
# find their sum 

import array as arr

def enter_data():
    a = arr.array('i',[])
    for i in range(5):#0 to 4 
        a.append(int(input("Enter a number to store in the array : ")))
    return a

def addition(a):
    s = 0
    for j in range(5):#0 to 4 
        s += a[j] # 2,3,4,5,6,7
    print("The array is : ",a)
    print("Sum of the number is = "+str(s))

if __name__=="__main__":
    a = enter_data()
    addition(a)
