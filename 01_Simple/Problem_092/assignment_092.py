'''
Write A Python Program To Find 
Celling And Floor Of A Number
'''


import math

if __name__=="__main__":
    num = float(input("Enter a number : "))
    print("The Celling of number is : ",math.ceil(num))
    print("The Floor of number is   : ", math.floor(num))