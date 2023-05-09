'''
Write a Python Program to get 5 number from user in array, AND find maximum number.
'''
import array as arr

def enter_data():
    a = arr.array('i',[])
    for i in range(5):#0 to 4 
        a.append(int(input("Enter a number to store in the array : ")))
    return a

def maximun(a):
    return max(a)

if __name__=="__main__":
    a = enter_data()
    print("The max element of  array is : ",maximun(a))
