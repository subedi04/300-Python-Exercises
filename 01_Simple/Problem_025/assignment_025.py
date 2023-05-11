'''
Write A Python Program To Get Student Name , 
If Student Name Is “xyz”, Then Don’t Allow Him To Take Admission
'''

def Allow_Admin_Name(name):
    if name=="xyz":
        print("Yo can't to take admission")
    else:
        print("Welcome to Admission")

if __name__=="__main__":
    name = input("Enter your name : ")
    Allow_Admin_Name(name)