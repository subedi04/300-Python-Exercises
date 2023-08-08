'''
Write a Python Program to find maximum and 
minimum number from a excel file
'''

import pandas as pd

if __name__=="__main__":
    file = pd.read_excel("problem66.xlsx")
    m = file["marks"].max()
    mn = file["marks"].min()
    print("Max = "+str(m))
    print("Min = "+str(mn))
