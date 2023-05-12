'''
Write A Python Program To Get A  Number From User To Check, 
It Is Divisible By 5 And 6
'''
def Div_Five_Six(num):
    if(num%5 == 0 and num%6== 0):
        print("Number is divisbile by 5 and 6")
    else:
        print("Not a reqauired Number")

if __name__=="__main__":
    num = int(input("Enter a number : "))
    Div_Five_Six(num)
