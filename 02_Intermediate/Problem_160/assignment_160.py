'''
Write a Python Pandas program to compare two Numpy array.
'''
import pandas as pd
import numpy as np

def compare_numpy_arrays(arr1, arr2):
    # Creating Pandas Series from NumPy arrays
    series1 = pd.Series(arr1)
    series2 = pd.Series(arr2)

    # Using '==' operator to compare two Pandas Series
    are_equal_operator = (series1 == series2).all()

    # Using 'equals()' method to compare two Pandas Series
    are_equal_method = series1.equals(series2)

    return are_equal_operator, are_equal_method

if __name__=="__main__":
    array1 = np.array([10, 20, 30, 40, 50])
    array2 = np.array([10, 20, 30, 40, 50])
    array3 = np.array([10, 20, 30, 40, 60])

    # Comparing arrays
    result1, result2 = compare_numpy_arrays(array1, array2)
    print("Comparison Result using '==':", result1)
    print("Comparison Result using 'equals()':", result2)

    result1, result2 = compare_numpy_arrays(array1, array3)
    print("\nComparison Result using '==':", result1)
    print("Comparison Result using 'equals()':", result2)
