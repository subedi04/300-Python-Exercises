'''
Write a Python Program to get 5 number from user in array, 
find the Minimum number
'''

import array as arr

def enter_data():
    a = arr.array('i',[])
    for i in range(5):#0 to 4 
        a.append(int(input("Enter a number to store in the array : ")))
    return a

def minimum(a):
    m = a[0] # 2,3,4,5,6
    for j in range(5):
        print(a[j])
        if(a[j] < m):
            m = a[j]
    print("Min Number = "+str(m))

if __name__=="__main__":
    a = enter_data()
    minimum(a)
