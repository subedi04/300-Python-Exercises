'''
Write a Python program to read a CSV file as a list
'''

import csv

if __name__=="__main__":
    file = open("problem172.csv",'r')
    read = csv.reader(file)
    print(read)
    for i in read:
        print(i)