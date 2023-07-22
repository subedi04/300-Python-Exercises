'''
Write a Python Program to create a one dimensional array.
'''

import array

def create_one_dimensional_array():
    # Create an array of integers
    one_dimensional_array = array.array('i', [1, 2, 3, 4, 5])
    return one_dimensional_array

if __name__=="__main__":
    my_array = create_one_dimensional_array()

    print(my_array)
