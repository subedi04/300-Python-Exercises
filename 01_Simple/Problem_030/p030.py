'''
Write A Python Program To Get A  Number 
From User To Check, It Is Divisible By 2 And 3
'''
# to get a number 
# divisbile by 2 and 3

def Div_Two_Three(num):
    if(num%2 == 0 and num%3 == 0):
        print("Number is divisbile by 2 and 3")
    else:
        print("Not a reqauired Number")

if __name__=="__main__":
    num = int(input("Enter a number : "))
    Div_Two_Three(num)

