'''
Write A Python Program To Get Different Information Of Students
From User And Display All The Student Information In This Order. 
And After Displaying, Update User CNIC, Age And Contact, 
Then Display Updated Result.

 >>> 1) Name			---------
 >>> 2) Father Name     ---------
 >>> 3) CNIC			---------
 >>> 4) Age 			---------
 >>> 5) Contact	 		---------
'''

def get_student_information():
    student_info = {
        "Name": "",
        "Father Name": "",
        "CNIC": "",
        "Age": "",
        "Contact": ""
    }

    for key in student_info:
        value = input(f"Enter {key}: ")
        student_info[key] = value

    return student_info


def display_student_information(student_info):
    print("Student Information:")
    for key, value in student_info.items():
        print(f"{key}: {value}")


def update_student_information(student_info):
    print("Update Student Information:")
    for key in ("CNIC", "Age", "Contact"):
        value = input(f"Enter updated {key}: ")
        student_info[key] = value


if __name__=="__main__":
    # Get student information from the user
    student_information = get_student_information()

    # Display the initial student information
    display_student_information(student_information)

    # Update student information
    update_student_information(student_information)

    # Display the updated student information
    print("Updated Student Information:")
    display_student_information(student_information)