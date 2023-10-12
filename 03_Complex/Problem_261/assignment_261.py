'''
Write a Python Program to make List of students to a text file
'''

students = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve"
]


file_path = 'students.txt'

try:
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write each student's name to the file
        for student in students:
            file.write(student + '\n')

    print(f"Student names have been written to '{file_path}'.")
except IOError as e:
    print(f"An error occurred: {e}")
