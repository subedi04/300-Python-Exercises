'''
Write a Python Numpy program to 
check element whether it is NaN or not.
'''
import numpy as np

if __name__=="__main__":
    ar = np.array([1,2,3,4,5,6,np.nan, np.inf])
    print(np.isnan(ar))