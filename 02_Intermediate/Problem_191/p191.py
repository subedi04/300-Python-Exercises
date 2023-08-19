'''
Write a Python program to get a string from 
user which contain number at starting and 
ending position.
'''

import re 

if __name__=="__main__":
	text = input("Enter a string : ")
	x = re.search('^[0-9]+[a-zA-Z]*[0-9]+$', text)
	if x:
		  print("Valid, start and end with number")
	else:
		  print("Not valid")
