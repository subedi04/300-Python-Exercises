'''
Write a Python Program to Get a string from user to 
find a sequence of number having 5 length or more.
'''
import re

text = "adshfaskl32khskldkf88asdfk83ksdk8384kdfsjasd34983394348"
x = re.search("[0-9]{5}",text)
if x:
    print("Matching...")
else:
    print("Not Matching")