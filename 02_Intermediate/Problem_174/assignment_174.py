'''
Write a Python Program to Delete cell value of CSV.
'''

import csv

def delete_csv_cell_value(file_path, row_index, column_index):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
    
    if row_index < len(data) and column_index < len(data[row_index]):
        data[row_index][column_index] = ""
        
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
        print("Cell value deleted successfully.")
    else:
        print("Invalid row or column index.")

if __name__=="__main__":
    file_path = 'your_file.csv'
    row_index = int(input("Enter row index: "))
    column_index = int(input("Enter column index: "))

    delete_csv_cell_value(file_path, row_index, column_index)
