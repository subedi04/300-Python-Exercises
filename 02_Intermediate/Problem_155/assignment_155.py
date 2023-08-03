'''
Write a Python Program to reshape an array
'''

import numpy as np

def reshape_array(arr, rows, cols):
    try:
        reshaped_arr = np.reshape(arr, (rows, cols))
        return reshaped_arr
    except ValueError:
        return "Cannot reshape array with given dimensions"

if __name__=="__main__":
    arr = np.array([1, 2, 3, 4, 5, 6])
    rows = 2
    cols = 3

    reshaped_arr = reshape_array(arr, rows, cols)
    print(reshaped_arr)
