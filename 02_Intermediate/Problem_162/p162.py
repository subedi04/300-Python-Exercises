'''
Write a Python program to convert array 
float data type to integer data type.
'''

import numpy as np

if __name__=="__main__":
    ar = np.array([
        [2.3, 5.2],
        [4.1,5.3]
    ])
    print(ar)
    new_ar = ar.astype("int")
    print(new_ar)