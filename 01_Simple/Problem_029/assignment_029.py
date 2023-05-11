'''
Write A Python Program To Get Number To Check, 
Whether It Is Positive, Negative Or Equal To Zero 
'''

def Pos_Neg(num):
    if num == 0:
        print("Your number is 0")
    elif(num > 0):
        print(str(num)+" is the Positive")
    else:
        print(str(num)+" is the Negative")

if __name__=="__main__":
    num = int(input("Enter a number : ")) # '5' ->5
    Pos_Neg(num)