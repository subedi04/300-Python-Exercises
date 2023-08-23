'''
Write a Python Program to display odd number from array.
'''

from array import *

if __name__=="__main__":
	ar = array('i',[1,10,8,13,4,5,6,7])
	print(ar)

	for i in ar:
		  if i%2 != 0:
		      print(i)

