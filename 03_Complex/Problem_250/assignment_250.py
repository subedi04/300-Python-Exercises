'''
Write a regular expression Program in Python 
to search following pattern inside a string: 
anythingNumber_Uppercase
'''

import re

pattern = r"[a-zA-Z0-9]+_[A-Z]+"

text = "This is a string with the pattern 'anythingNumber_Uppercase'."

match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")
