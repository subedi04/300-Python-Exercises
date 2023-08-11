'''
Write a Python Program to get column names from CSV. Using another method.
'''

import csv

def get_column_names(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        column_names = reader.fieldnames

    return column_names


if __name__=="__main__":
    csv_file = 'data.csv'

    column_names = get_column_names(csv_file)
    if column_names:
        print("Column names:", column_names)
    else:
        print("No columns found in the CSV.")
