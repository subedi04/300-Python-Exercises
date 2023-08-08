'''
Write a Python Program to read s
pecific column data from excel.
'''

import pandas as pd

if __name__=="__main__":
    col = [1,2,3]
    e = pd.read_excel("xlswriter_wb2.xlsx", usecols=col)
    print(e)
