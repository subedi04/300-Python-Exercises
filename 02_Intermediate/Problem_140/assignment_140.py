'''
Write a NumPy program to create one-dimensional array, 
getting number element from user using while loop.
'''

import numpy as np

def create_1d_array():
    elements = []
    
    print("Enter elements for the one-dimensional array. Enter 'done' to finish.")
    while True:
        try:
            user_input = input("Enter an element (or 'done' to finish): ")
            if user_input.lower() == 'done':
                break
             # You can use int() if you want to create an array of integers.
            element = float(user_input) 
            elements.append(element)
        except ValueError:
            print("Invalid input! Please enter a numeric value or 'done' to finish.")

    one_dim_array = np.array(elements)
    return one_dim_array

def main():
    one_dim_array = create_1d_array()
    print("One-dimensional array:")
    print(one_dim_array)

if __name__ == "__main__":
    main()
