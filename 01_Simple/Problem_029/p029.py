# get a number 
# check, negative or positve 

def Pos_Neg(num):
    if(num > 0):
        print(str(num)+" is the Positive")
    else:
        print(str(num)+" is the Negative")


if __name__== "__main__":
    num = int(input("Enter a number")) # '5' ->5
    Pos_Neg(num)
