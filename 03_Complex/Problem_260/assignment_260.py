'''
Write a Python Program to Read content from one file and write it 
into another file. Except a specific string, that is taken from user.
'''

string_to_exclude = input("Enter the string to exclude: ")

# Replace 'input_file.txt' with the path to your source file
input_file_path = 'input_file.txt'

# Replace 'output_file.txt' with the path to your target file
output_file_path = 'output_file.txt'

try:
    with open(input_file_path, 'r') as input_file:
        # Read the content of the source file
        content = input_file.read()

        # Remove the specific string entered by the user
        modified_content = content.replace(string_to_exclude, '')

        with open(output_file_path, 'w') as output_file:
            # Write the modified content to the target file
            output_file.write(modified_content)

    print(f"File '{input_file_path}' has been read, modified, and written to '{output_file_path}'.")
except FileNotFoundError:
    print(f"File not found: {input_file_path}")
