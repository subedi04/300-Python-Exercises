'''
Write a Python program to load csv file using other than pandas library and 
print the shape of the csv file and display data in the form of string.  
'''

import csv

def load_csv(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

def csv_shape(data):
    num_rows = len(data)
    num_columns = len(data[0]) if num_rows > 0 else 0
    return num_rows, num_columns

def display_csv(data):
    for row in data:
        print(','.join(row))

if __name__ == "__main__":
    csv_file = "sample.csv"  # Replace with your CSV file path
    
    loaded_data = load_csv(csv_file)
    
    shape = csv_shape(loaded_data)
    print(f"CSV Shape (rows, columns): {shape}")
    
    print("\nCSV Data:")
    display_csv(loaded_data)
