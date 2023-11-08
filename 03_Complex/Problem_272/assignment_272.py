'''
Write a Python Program To remove a file.
'''
import os

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been successfully removed.")
    except OSError as e:
        print(f"Error: {e}")
        
# Specify the file path you want to remove
file_to_remove = "path/to/your/file.txt"

remove_file(file_to_remove)
