'''
Write a Python Numpy program to convert 
a given list into an array, 
then again convert it into a list. 
'''

import numpy as np

def list_to_array_to_list(input_list):
    # Convert the given list to a NumPy array
    array_data = np.array(input_list)

    # Convert the NumPy array back to a Python list
    output_list = array_data.tolist()

    return output_list

if __name__=="__main__":
    given_list = [1, 2, 3, 4, 5]
    result_list = list_to_array_to_list(given_list)
    print("Given List:", given_list)
    print("Resulting List:", result_list)
