'''
Write a Python Numpy program to create a 4x4 
zero matrix with elements on the main diagonal
 equal to 6, 7, 8, 9. 
'''
import numpy as np

if __name__=="__main__":
    arr = np.diag([1,2])
    print(arr)