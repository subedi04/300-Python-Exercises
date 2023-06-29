"""
Write A Python Program To Store 5 Student Name 
In A List And Check If The First Char Of 
First Student Name Is Equal To Last Student’s First Char
"""

def check_first_char(names):
    if names[0].lower() == names[-1].lower():
        return True
    else:
        return False

# Store student names in a list
def get_data():
    student_names = []
    for i in range(5):
        name = input("Enter student name: ")
        student_names.append(name)
    return student_names

# Check if the first character of the first student's name is equal to the first character of the last student's name
if __name__=="__main__":
    student_names = get_data()
    result = check_first_char(student_names)

    # Print the result
    if result:
        print("The first character of the first student's name is equal to the first character of the last student's name.")
    else:
        print("The first character of the first student's name is not equal to the first character of the last student's name.")
