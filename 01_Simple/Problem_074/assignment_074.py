'''
Write A Python Program To 
Find The Second Position Of 
A Student In A List. 
And Display Student Marks 
And Student Name
'''

def find_second_position(students):
    """
    Finds the second position of a student in a list and displays their marks and name.
    
    Parameters:
        students (list): List of students' information.
    
    Returns:
        None
    """
    if len(students) < 2:
        print("Insufficient number of students.")
        return
    
    # Sort students based on marks in descending order
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    
    # Get the second student from the sorted list
    second_student = sorted_students[1]
    
    # Extract student information
    student_name = second_student[0]
    student_marks = second_student[1]
    
    # Display student marks and name
    print("Second Position Student:")
    print("Name:", student_name)
    print("Marks:", student_marks)

if __name__=="__main__":
    # Sample list of students' information [name, marks]
    students = [
        ["Alexander", 85],
        ["Elizabeth", 92],
        ["Michael", 78],
        ["Danner", 90],
        ["Miguel", 88]
    ]

    # Find and display the second position student
    find_second_position(students)
