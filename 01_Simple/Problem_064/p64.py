'''
Write A Python Program To Find Scholarship For Students 
In Admission In A College On The Basis Of Student Marks.

Criteria To Follow
Marks Equal To 1100 	Free Education
Marks > 1000	 	80%  Monthly Fees Deduction
Marks > 900		60%  Monthly Fees Deduction
Marks > 800		40%  Monthly Fees Deduction
Marks > 700		30%  Monthly Fees Deduction
Marks > 600		There Is No Scholarship 
'''

"""
Marks Equal To 1100 	Free Education
Marks > 1000	 	80%  Monthly Fees Deduction
Marks > 900		60%  Monthly Fees Deduction
Marks > 800		40%  Monthly Fees Deduction
Marks > 700		30%  Monthly Fees Deduction
Marks > 600		There Is No Scholarship 
"""
def scholarship(marks):
    if(marks == 1100):
        print("Free Education")
    elif (marks > 1000):
        print("80%  Monthly Fees Deduction")
    elif (marks > 900):
        print("60%  Monthly Fees Deduction")
    elif (marks > 800):
        print("40%  Monthly Fees Deduction")
    elif (marks > 700):
        print("30%  Monthly Fees Deduction")  
    elif (marks > 600):
        print("There Is No Scholarship")
    else:
        print("Enter valid number")

if __name__ == "__main__":
    marks = int(input("Enter your marks : "))
    scholarship(marks)