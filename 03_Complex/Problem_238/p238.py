'''
Write a Python program to get a string from user 
that have starting char f and ending char z (zero, one or many z).
'''

import re

s = input("Enter a string : ")

x = re.search('^f(z*)$' ,s)

if x:
    print("Matching....")
else:
    print("Not Matching")