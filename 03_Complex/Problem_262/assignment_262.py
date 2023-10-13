'''
Write a Python Program to check file size. 
Display message if file size between 3 to 5 Mb.
'''

import os

file_path = 'your_file.txt'

file_size_bytes = os.path.getsize(file_path)

# Convert the file size to megabytes
file_size_mb = file_size_bytes / (1024 * 1024)

lower_limit = 3  # 3 MB
upper_limit = 5  # 5 MB

if lower_limit <= file_size_mb <= upper_limit:
    print(f"The file size is between {lower_limit} MB and {upper_limit} MB.")
else:
    print(f"The file size is not between {lower_limit} MB and {upper_limit} MB.")
