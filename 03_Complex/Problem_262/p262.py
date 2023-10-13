'''
Write a Python Program to check file size.
'''

import os.path

file = "filedict.txt"
size = os.path.getsize(file)
print(str(size)+" bytes")