'''
Write a Python Numpy Program to Create 
a array of zero. According to user entered number.
'''

import numpy as np

if __name__=="__main__":
    z = int(input("Enter a number : "))
    ar = np.zeros(z)
    print(ar) 