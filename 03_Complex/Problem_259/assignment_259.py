'''
Write a Python Program to get file creation and modification date or time
'''

import os

file_path = 'your_file.txt'

try:
    # Get the file's creation time (only available on Windows)
    if os.name == 'nt':
        creation_time = os.path.getctime(file_path)
        print(f'File creation time: {creation_time}')
    else:
        print('File creation time is not available on this platform.')

    # Get the file's modification time
    modification_time = os.path.getmtime(file_path)
    print(f'File modification time: {modification_time}')
except FileNotFoundError:
    print(f'File not found: {file_path}')
