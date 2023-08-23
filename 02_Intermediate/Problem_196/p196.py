'''
Write a Python Program to remove any specific element from array.
'''

from array import *

if __name__=="__main__":
	ar = array('i',[1,10,8,13,4,5,6,7])
	print(ar)
	n = int(input("Enter position of element which you want to remove : "))
	ar.pop(n-1) #2, 3-1 = 2
	print(ar)
