'''
Write a Python Pandas program to find transpose of array
'''

import numpy as np

if __name__=="__main__":
    ar = np.array([
        [2,3],
        [4,5]
    ])
    print(ar)
    t_ar = ar.T
    print(t_ar)