'''
Write a Python Numpy Program to generate 
one particular value of a matrix
'''

import numpy as np

# Function to generate a matrix with a particular value
def generate_matrix(rows, cols, value):
    matrix = np.full((rows, cols), value)
    return matrix

if __name__=="__main__":
    rows = 3
    cols = 4
    value = 5

    matrix = generate_matrix(rows, cols, value)
    print(matrix)
