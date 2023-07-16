'''
Write a Python program to find 
most occurring element in a given 
list of numbers.
'''
from statistics import mode

if __name__=="__main__":
    lst = [11,2,3,3,1,1,2,3,4,5,6,7,9]
    print(lst)
    print(mode(lst))
