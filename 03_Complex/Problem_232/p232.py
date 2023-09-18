'''
Write a Python program to load csv file using pandas 
and print the shape of the csv file and display data 
in the form of string. 
'''

import pandas as pd

if __name__=="__main__":
    file = pd.read_csv("myfile.csv")
    print(file.shape)
    print(file.to_string)