'''
Write a Python program to read an excel file using other than xlwings 
'''

import pandas as pd

if __name__=="__main__":
    excel_file = 'path/to/your/excel/file.xlsx'

    df = pd.read_excel(excel_file)
    print(df)
