'''
Write a Python Program to count any array element from existed array.
'''

from array import *
if __name__=="__main__":
	ar = array('i',[1,1,1,13,4,5,6,7])
	print(ar)
	n = int(input("Enter a number : "))
	result = ar.count(n)
	print(str(result)+ " time "+str(n)+" existed")
