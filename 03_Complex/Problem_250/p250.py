'''
Write a regular expression Program in Python 
to search following pattern inside a string: 
anything(optional)Number_Uppercase
'''
import re

str = input("Enter a str : ")

# anything number _ uppercase
x = re.search('.*[0-9]+[_]+[A-Z]+', str)

if x:
    print("Matching..")
else:
    print("Not Matching..")