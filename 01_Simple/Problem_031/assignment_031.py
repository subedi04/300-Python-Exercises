'''
Write A Python Program To Get Scale From Employer And Then Display Salary According To Employer Scale
Using This Criteria, If:
    Scale Is 9, display 10,000
    Scale Is 12 , display 20,000
    Scale Is 15 , display 40,000
    Scale Is 18 , display 50,000
    Scale Is 20 , display 70,000
'''

def Salary(scale):
    if scale == 9 : 
        print("Your salary is 10,000")
    elif scale == 12 :
        print("Your salary is 20,000")
    elif scale == 15:
        print("Your salary is 40,000")
    elif scale == 18 : 
        print("Your salary is 50,000")
    elif scale == 20 :
        print("Your salary is 70,000")
    else:
        print("Enter a correct scale")

def Info():
    print("****************************************")
    print("**                                    **")  
    print("**               SALARY               **")
    print("**                                    **")  
    print("****************************************")
    print("\n")
    print("Chose your scale: ")
    print(">>> Scale 9")
    print(">>> Scale 12")
    print(">>> Scale 15")
    print(">>> Scale 18")
    print(">>> Scale 20")
    print("\n")


if __name__=="__main__":
    Info()
    scale = int(input("Enter your scale : "))
    Salary(scale)
