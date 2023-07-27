'''
Write a Python NumPy program to Subtract two array.
'''

import numpy as np

def main():
    # Example arrays
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([5, 4, 3, 2, 1])

    # Method 1: Using the "-" operator
    result_subtract_operator = array1 - array2

    # Method 2: Using np.subtract()
    result_np_subtract = np.subtract(array1, array2)

    print("Array 1:", array1)
    print("Array 2:", array2)
    print("Result using '-' operator:", result_subtract_operator)
    print("Result using np.subtract():", result_np_subtract)

if __name__ == "__main__":
    main()

'''
Array 1: [1 2 3 4 5]
Array 2: [5 4 3 2 1]
Result using '-' operator: [-4 -2  0  2  4]
Result using np.subtract(): [-4 -2  0  2  4]

'''