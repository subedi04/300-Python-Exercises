'''
Write a Python program to match a number and _ at the ending of a string. 
'''

import re

pattern = r"([0-9]+)\_"


matches = re.findall(pattern, "This is a string with a number 123_ at the end.")


for match in matches:
    print(match)
