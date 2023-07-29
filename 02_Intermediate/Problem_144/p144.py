'''
Write a Python Numpy program to convert 
array element to Boolean value
'''
import numpy as np

if __name__=="__main__":
    # ar = np.array([1,1,1,0,0,1,0,1])
    ar = np.array([
        [1,0],
        [0,1]
    ])
    print(ar)
    bool_arr = ar.astype('bool')
    print(bool_arr)