'''
Write a NumPy program to create a new array of 
given shape (4,3) and type, filled with ones. 
And make in such way, user give shape value 
on run time.
'''

import numpy as np

def create_ones_array():
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            break
        except ValueError:
            print("Invalid input! Please enter integer values for rows and columns.")

    ones_array = np.ones((rows, cols), dtype=np.int64)
    return ones_array

def main():
    ones_array = create_ones_array()
    print("Array of ones:")
    print(ones_array)

if __name__ == "__main__":
    main()
