'''
Write a Python NumPy program to save a given array 
to a text file and load it. Using another method.
'''

import numpy as np

def save_array_to_text_file(array, file_path):
    np.savetxt(file_path, array)

def load_array_from_text_file(file_path):
    return np.loadtxt(file_path)


def save_array_to_binary_file(array, file_path):
    np.save(file_path, array)

def load_array_from_binary_file(file_path):
    return np.load(file_path)


if __name__=="__main__":
    original_array = np.array([1, 2, 3, 4, 5])

    print("\t Method 1")

    save_array_to_text_file(original_array, "data_m1.txt")

    # Load the array from the text file
    loaded_array_m1 = load_array_from_text_file("data_m1.txt")

    # Print the original and loaded arrays
    print("Original Array:", original_array)
    print("Loaded Array:", loaded_array_m1)




    print("\t Method 2")
    save_array_to_binary_file(original_array, "data_m2.npy")

    # Load the array from the binary file
    loaded_array_m2 = load_array_from_binary_file("data_m2.npy")

    # Print the original and loaded arrays
    print("Original Array:", original_array)
    print("Loaded Array:", loaded_array_m2)
