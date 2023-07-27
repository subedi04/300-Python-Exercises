'''
Write a NumPy program to create one-dimensional array, 
getting number element from user using for loop.
'''

import numpy as np

if __name__=="__main__":
    num = int(input("Enter a number : ")) # 6
    ar = np.zeros(num, dtype=np.int64) # 6

    for i in range(len(ar)):
        element = int(input("Enter array element : "))
        ar[i] = element
    print(ar)