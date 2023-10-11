'''
Write a Python Program to print the memory usage of object
'''

import sys
s = input("Enter a string type of data : ")
size = sys.getsizeof(s)
print(size)