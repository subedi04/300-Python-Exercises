'''
Write a Python Numpy Program To Multiply Two Array.
'''

import numpy as np

def main():
    # Example arrays
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([2, 4, 6, 8, 10])

    # Method 1: Using the "*" operator
    result_multiply_operator = array1 * array2

    # Method 2: Using np.multiply()
    result_np_multiply = np.multiply(array1, array2)

    print("Array 1:", array1)
    print("Array 2:", array2)
    print("Result using '*' operator:", result_multiply_operator)
    print("Result using np.multiply():", result_np_multiply)

if __name__ == "__main__":
    main()
