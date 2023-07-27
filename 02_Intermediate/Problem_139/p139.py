'''
Write a NumPy program to create a new array 
of given shape (4,3) and type, filled with zeros. 
'''

import numpy as np

if __name__=="__main__":
    ar = np.zeros( (3,3), dtype=np.int64)
    print(ar)