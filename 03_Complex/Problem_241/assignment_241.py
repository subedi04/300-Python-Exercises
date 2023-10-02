"""
Write a Python program that matches a string that 
has an ‘m or M' followed by anything, ending in ‘0 or 1'. 
"""
import re

def match_pattern(string):
    pattern = r'[mM].*[01]$'
    match = re.match(pattern, string)
    return match is not None


if __name__=="__main__":
    strings = ['m0', 'M1', 'M2', 'm3', 'abcM1', 'xyzm0']
    for string in strings:
        if match_pattern(string):
            print(f"{string}: Match")
        else:
            print(f"{string}: No match")
