'''
Write a Python Numpy Program to create a one dimensional array element. 
Then convert to list and then to tuple. 
'''

import numpy as np

if __name__=="__main__":
    numpy_array = np.array([1, 2, 3, 4, 5])

    list_from_array = numpy_array.tolist()

    tuple_from_list = tuple(list_from_array)

    numpy_array, list_from_array, tuple_from_list
