'''
Write a Python Program to perform 
different operation on excel file
'''

import pandas as pd

if __name__=="__main__":
    file = pd.read_excel("problem168.xlsx")
    sum = file["price"].sum()
    product = file["price"].product()
    count = file["price"].count()
    mean = file["price"].mean()
    print("Total Sum = "+str(sum))
    print("Total Product = "+str(product))
    print("Total Values = "+str(count))
    print("Total Mean = "+str(mean))
