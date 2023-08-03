'''
Write a Python Numpy Program to replace any number in Array.
'''
import numpy as np 

if __name__=="__main__":
    ar = np.array([1,2,3,4,5,6,7,8,9,10])
    print(ar)
    ar[ar%2 == 0] = -1
    print(ar)