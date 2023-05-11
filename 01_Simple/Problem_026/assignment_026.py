'''
Write A Python Program To Check A Number, 
Whether It Is Even Or Odd Number And Then Find That Number Square
'''

def even_odd(num):
    if (num%2 == 0):# 10, 17%2->1
        print("Number is even")
    else:
        print("Number is odd")

def square(num):
    print("The square of number is : ", pow(num,2))
if __name__=="__main__":
    num = int(input("Enter a number : "))
    print("\n")
    even_odd(num)
    print("\n")
    square(num)