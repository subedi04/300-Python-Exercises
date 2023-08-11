'''
Write a Python Program to get column names from CSV.
'''


import filecmp
import pandas as pd

if __name__=="__main__":
    file = pd.read_csv("problem176.csv")
    file_col = file.columns
    print(file_col)