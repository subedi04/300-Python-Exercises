'''
Write a Numpy Program To Create a one dimensional array. 
Display only even number from array.
'''

import numpy as np

def create_1d_array():
    elements = []
    size = int(input("Enter the size of the one-dimensional array: "))

    print("Enter elements for the one-dimensional array:")
    for i in range(size):
        try:
            element = int(input(f"Element {i+1}: "))
            elements.append(element)
        except ValueError:
            print("Invalid input! Please enter an integer.")

    one_dim_array = np.array(elements)
    return one_dim_array

def display_even_numbers(arr):
    even_numbers = arr[arr % 2 == 0]
    return even_numbers

def main():
    one_dim_array = create_1d_array()
    print("One-dimensional array:", one_dim_array)

    even_numbers_array = display_even_numbers(one_dim_array)
    print("Even numbers from the array:", even_numbers_array)

if __name__ == "__main__":
    main()
