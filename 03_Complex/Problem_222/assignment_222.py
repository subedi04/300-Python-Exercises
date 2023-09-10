"""
Write A Python Program To Get File Name 
From User If File Name Have Space Then 
Replace Space With 'Dot' Symbol
"""

def get_modified_filename():
    file_name = input("Enter the file name: ")
    modified_name = file_name.replace(" ", ".")

    return modified_name

if __name__ == "__main__":
    modified_name = get_modified_filename()
    print(f"Modified file name: {modified_name}")
