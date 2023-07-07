'''
Write A Python Program To Get 10 Name Of The Students 
And Display Them On The Screen And User Able To Update 
Any Student On Run Time
'''

def get_student_names():
    student_names = []
    for i in range(10):
        name = input(f"Enter the name of student {i + 1}: ")
        student_names.append(name)
    return student_names

def display_student_names(student_names):
    print("Student Names:")
    for i, name in enumerate(student_names, start=1):
        print(f"Student {i}: {name}")

def update_student_name(student_names):
    index = int(input("Enter the index of the student to update (1-10): "))
    if 1 <= index <= 10:
        new_name = input("Enter the new name: ")
        student_names[index - 1] = new_name
        print("Student name updated successfully.")
    else:
        print("Invalid index.")

if __name__=="__main__":
    student_names = get_student_names()
    display_student_names(student_names)

    while True:
        choice = input("Do you want to update a student's name? (yes/no): ")
        if choice.lower() == "yes":
            update_student_name(student_names)
            display_student_names(student_names)
        elif choice.lower() == "no":
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    print("Program ended.")
