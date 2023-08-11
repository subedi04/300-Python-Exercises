'''
Write a Python Program to delete any row in a CSV file
'''

import csv

def delete_row(csv_file, row_index):
    rows = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    if row_index < 0 or row_index >= len(rows):
        print("Invalid row index.")
        return

    deleted_row = rows.pop(row_index)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Row deleted:", deleted_row)

if __name__=="__main__":
    # Replace 'data.csv' with your CSV file's name and provide the row index you want to delete.
    csv_file = 'data.csv'
    row_to_delete = 2  # Index of the row to delete (0-based)

    delete_row(csv_file, row_to_delete)
