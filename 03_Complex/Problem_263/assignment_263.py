'''
Write a Python Program to read specific lines 
from a File. More than one line should be display.
'''


if __name__=="__main__":
    file_path = 'your_file.txt'


    lines_to_read = [2, 4, 6]

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            for line_number in lines_to_read:
                # Check if the line number is within the valid range
                if 1 <= line_number <= len(lines):
                    line = lines[line_number - 1]
                    print(f"Line {line_number}: {line.strip()}")
                else:
                    print(f"Line {line_number} is out of range.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
