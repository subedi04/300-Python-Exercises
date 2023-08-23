'''
Write a Python Program to Reverse array element.
'''

from array import *

if __name__=="__main__":
	ar = array('i',[1,10,8,13,4,5,6,7])

	print(ar)
	ar.reverse()
	print(ar)
	for i in ar:
		  print(i)
