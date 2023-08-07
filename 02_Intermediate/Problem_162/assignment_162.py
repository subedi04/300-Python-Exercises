'''
Write a Python Numpy Program to Check 
whether a array contains a specified row.
'''

import numpy as np

def is_row_present(arr, row):
    for r in arr:
        if np.array_equal(r, row):
            return True
    return False


if __name__=="__main__":
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    row1 = np.array([4, 5, 6])
    row2 = np.array([2, 3, 4])

    print(is_row_present(arr, row1))  # Output: True
    print(is_row_present(arr, row2))  # Output: False
