'''
Write a Python Numpy Program to get Two Dimensional Array 
input from user to Display 2D Array using while Loop.
'''

import numpy as np

def get_2d_array_from_user():
    rows = int(input("Enter the number of rows in the 2D array: "))
    cols = int(input("Enter the number of columns in the 2D array: "))
    
    arr = np.empty((rows, cols), dtype=np.int)
    row = 0

    print("Enter the elements row-wise:")

    while row < rows:
        col = 0
        while col < cols:
            try:
                value = int(input(f"Enter element at position ({row}, {col}): "))
                arr[row, col] = value
                col += 1
            except ValueError:
                print("Invalid input! Please enter an integer.")
        row += 1

    return arr

def display_2d_array(arr):
    rows, cols = arr.shape
    print("2D Array:")
    for row in range(rows):
        for col in range(cols):
            print(arr[row, col], end=" ")
        print()

if __name__ == "__main__":
    array_2d = get_2d_array_from_user()
    display_2d_array(array_2d)
