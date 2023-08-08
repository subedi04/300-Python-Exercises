'''
Write a Python program to read an excel file using xlwings
'''

import xlwings

if __name__=="__main__":
    wb = xlwings.Book("xlwings.xlsx").sheets["Sheet1"]
    data = wb.range("A2").value
    print(data)