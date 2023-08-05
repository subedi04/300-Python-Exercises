'''
Write a Python Pandas program to convert 
a Pandas series to Numpy array.
'''

import pandas as pd
import numpy as np

def pandas_series_to_numpy(series):
    return series.values

if __name__=="__main__":
    data = pd.Series([10, 20, 30, 40, 50])

    # Converting to NumPy array
    numpy_array = pandas_series_to_numpy(data)

    print("Pandas Series:")
    print(data)

    print("\nNumPy Array:")
    print(numpy_array)
