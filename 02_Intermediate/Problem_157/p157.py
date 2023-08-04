'''
Write a Python Program to append 
array element to existing array. 
'''
from array import * 

if __name__=="__main__":
    ar = array('i',[1,2,3,4,6,5])
    print(ar)
    item = int(input("Enter element : "))
    ar.append(item)
    print(ar)