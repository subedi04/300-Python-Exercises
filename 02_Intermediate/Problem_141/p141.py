'''
Write a Numpy Program To Create a Two-dimensional Array & 
Multiply with any number to that array elements. 
That number take from user.
'''
import numpy as np

if __name__=="__main__":
    ar = np.array([
        [1,2,3],
        [4,5,6],
        [4,1,6]
    ])
    print(ar)
    item = int(input("Enter a number : "))
    new_ar = item*ar
    print(new_ar)