'''
Write a Python program to get two number and operator from the user to perform arithmetic operation. 
And if user provide operator other than arithmetic then restrict user. Using Function
'''

def Arithmetic_Ops(a,b,op):
    print("\n")
    if(op == '+'):
        print("Addition of two numbers is = "+str(a+b))
    elif(op == '-'):
        print("Subtraction of two numners is = "+str(a-b))
    elif(op == '/'):
        print("Division of two numbers is = "+str(a/b))
    elif(op == '*'):
        print("Multiplication of two numbers is = "+str(a*b))
    elif(op == '%'):
        print("Mod of two numbers is = "+str(a%b))
    else:
        print("Invalid Operator, please one of them as +, -, /, * and %")

def Get_Data():
    a = int(input(">>> Enter 1st number : ")) # 4
    b = int(input(">>> Enter 2nd number : ")) # 7
    op = input(">>> Insert a operator to perform operation : ") # /
    return a,b,op

def Info():
    print("\t*****************************************************************")
    print("\t**                                                             **")
    print("\t**                       BASIC OPERATIONS                      **")
    print("\t**                                                             **")
    print("\t*****************************************************************")

    print("You must enter 2 numbers and chose your operator\n")

    print("Operators \t Operation")
    print(" + \t\t addition")
    print(" - \t\t sustraction")
    print(" * \t\t multiplication")
    print(" / \t\t division")
    print(" % \t\t module")
    print("\n")

if __name__=="__main__":
    Info()
    a,b,op = Get_Data()
    Arithmetic_Ops(a,b,op)