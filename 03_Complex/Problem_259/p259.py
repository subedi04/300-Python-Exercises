'''
Write a Python Program to get file creation date or time.
'''

import os.path
import time

t = os.path.getctime("myfile.csv")
ctime = time.ctime(t)
print(ctime)
