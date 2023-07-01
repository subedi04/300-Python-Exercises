'''
Write A Python Program To Get A Number From User, 
The System Should Auto Decrement To That Number. 
Half Of User Entered Number Should Be Decremented
'''
def Decrement_number(number):
    while number > 0 :
        print(number)
        number -= 1


if __name__=="__main__":
    number = int(input("Enter a number: "))
    half_number = number // 2
    
    print("Decrementing the Orginal Number : ")
    print("Original Number : ", number)
    Decrement_number(number)

    print("\n ")

    print("Decrementing The Half Number ")
    print("Half Number : ", half_number)
    Decrement_number(half_number)


