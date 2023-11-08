'''
Write a Python Program to take a string 
from user to search in two file
'''

def search_string_in_files(file1, file2, search_string):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            file1_content = f1.read()
            file2_content = f2.read()

            if search_string in file1_content:
                print(f"String found in {file1}")
            else:
                print(f"String not found in {file1}")

            if search_string in file2_content:
                print(f"String found in {file2}")
            else:
                print(f"String not found in {file2}")

    except FileNotFoundError:
        print("One or both files not found.")

if __name__=="__main__":
    user_string = input("Enter the string to search: ")

    # Replace file paths with your file locations
    file_path_1 = 'path/to/your/file1.txt'
    file_path_2 = 'path/to/your/file2.txt'

    search_string_in_files(file_path_1, file_path_2, user_string)
