'''
Write A Python Program To Get Student Identity, 
System Should Help To Avoid Duplicate Identity Insertion
'''
def check_duplicate_identity(identities, identity):
    if identity in identities:
        return True
    else:
        return False


def get_student_identities():
    student_identities = []

    while True:
        identity = input("Enter a student identity (or 'q' to quit): ")

        if identity == 'q':
            break

        if check_duplicate_identity(student_identities, identity):
            print("Identity already exists! Please enter a different identity.")
        else:
            student_identities.append(identity)

    print("Student Identities:")
    for identity in student_identities:
        print(identity)


get_student_identities()
