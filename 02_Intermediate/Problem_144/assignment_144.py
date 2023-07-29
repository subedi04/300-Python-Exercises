'''
Write a Python NumPy program to convert an array to bytes and load it as array.
'''

import numpy as np

def array_to_bytes_and_load(arr):
    # Convert the array to bytes
    array_bytes = arr.tobytes()

    # Load the bytes as a new array
    loaded_array = np.frombuffer(array_bytes, dtype=arr.dtype)

    return loaded_array

if __name__=="__main__":
    original_array = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    loaded_array = array_to_bytes_and_load(original_array)
    print("Original Array:", original_array)
    print("Loaded Array:", loaded_array)
