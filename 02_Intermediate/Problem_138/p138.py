'''
Write a Python NumPy program to make an array 
of equal shape having same data type of a given array. 
'''
import numpy as np

ar = np.array([
    [1,2,3],
    [4,5,6],
    [4,1,6]
])
new_ar = np.zeros_like(ar)
print(new_ar)