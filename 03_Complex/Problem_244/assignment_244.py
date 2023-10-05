'''
Write a Python program which match a string 
that contains uppercase, numbers, and underscores.
 It should not Ignore white space.
'''

import re

pattern = r"[A-Z0-9_]+"

string = "This is a string with uppercase, numbers, and underscores."

match = re.search(pattern, string)

if match:
    print("Match found:", match.group())
else:
    print("No match found")
