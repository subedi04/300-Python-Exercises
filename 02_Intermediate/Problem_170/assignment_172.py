'''
Write a Python program to read a CSV file 
as a list using another method.
'''

import csv

def read_csv_as_list(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

if __name__=="__main__":
    file_path = 'your_file.csv'
    csv_data = read_csv_as_list(file_path)

    for row in csv_data:
        print(row)

