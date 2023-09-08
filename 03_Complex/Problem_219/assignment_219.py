'''
Write A Python Program To Create A CSV File 
To Store Odd Number As Generated From 200 To 100.
'''

import csv

odd_numbers = [i for i in range(200, 99, -1) if i % 2 != 0]


filename = "/mnt/data/odd_numbers.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Odd Numbers"])
    for num in odd_numbers:
        writer.writerow([num])


