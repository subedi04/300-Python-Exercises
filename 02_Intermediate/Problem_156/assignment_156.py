'''
Write a Python Numpy Program to display 
1 dimension array with equality gaps 
between a range.
'''

import numpy as np

def display_array(start, end, gap):
    # Calculate the number of elements in the array
    num_elements = int((end - start) / gap) + 1
    
    # Create the array using NumPy's arange function
    arr = np.arange(start, end + gap, gap)
    
    # Print the array
    print(arr)

if __name__=="__main__":
    start = 0
    end = 10
    gap = 2

    display_array(start, end, gap)
