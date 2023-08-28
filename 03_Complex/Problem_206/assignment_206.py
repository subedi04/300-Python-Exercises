'''
Write A Python Program To Get 
10 Student Name Store Into List. 
Display Student Name Randomly. 
Don’t Include That Student Name 
Which User Say.
'''

import random

def main():
    student_names = []
    
    # Get 10 student names from the user
    for i in range(10):
        name = input(f"Enter student name {i + 1}: ")
        student_names.append(name)
    
    # Get the student name to exclude
    exclude_name = input("Enter the student name to exclude: ")
    
    # Remove the excluded name from the list
    if exclude_name in student_names:
        student_names.remove(exclude_name)
    
    # Display a random student name
    if student_names:
        random_name = random.choice(student_names)
        print(f"The randomly selected student name is: {random_name}")
    else:
        print("No student names available after excluding.")

if __name__ == "__main__":
    main()
