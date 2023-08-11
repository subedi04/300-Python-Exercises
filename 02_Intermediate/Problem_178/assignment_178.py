'''
Write a Python program to get the size, 
permissions, owner, device of a specified path.
'''

import os

def get_file_info(path):
    try:
        # Get the size of the file or directory in bytes
        size = os.path.getsize(path)

        # Get the permissions of the file or directory in octal notation
        permissions = oct(os.stat(path).st_mode)[-4:]

        # Get the owner of the file or directory
        owner = os.stat(path).st_uid

        # Get the device that the file or directory resides on
        device = os.stat(path).st_dev

        return size, permissions, owner, device
    except FileNotFoundError:
        return None

def main():
    specified_path = input("Enter the path to a file or directory: ")

    file_info = get_file_info(specified_path)
    if file_info:
        size, permissions, owner, device = file_info
        print("Size:", size, "bytes")
        print("Permissions:", permissions)
        print("Owner:", owner)
        print("Device:", device)
    else:
        print("File or directory not found.")

if __name__ == "__main__":
    main()
