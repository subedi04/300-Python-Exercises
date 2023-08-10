'''
Write a Python Program to Update cell value of CSV.
'''

import pandas as pd

if __name__=="__main__":
    file = pd.read_csv("problem174.csv")
    file.loc[3, "age"] = 30
    file.loc[2, "name"] = "Faisal Jafri"
    file.to_csv("problem72.csv")
    print(file)