'''
Write a Python program where a string will start with a specific number.  
'''
import re

str = input("Enter a str : ")

# string should start with a number
x = re.search('^[0-9]+', str)

if x:
    print("Matching....")
else:
    print("Not Matching")