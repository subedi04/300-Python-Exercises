'''
Write a Python Pandas program to convert a 
Numpy array to a Pandas series.
'''
import numpy as np
import pandas as pd

if __name__=="__main__":
    ar = np.array([1,2,3,4,5,6,7])
    print(ar)
    ps = pd.Series(ar)
    print(ps)