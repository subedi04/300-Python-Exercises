'''
Write A Python Program To Check A Number, 
Whether It Is Even Or Odd Number
'''
# to get a number from the user
# check even or odd
def even_odd(num):
    if (num%2 == 0):# 10, 17%2->1
        print("Number is even")
    else:
        print("Number is odd")

if __name__=="__main__":
    num = int(input("Enter a number : "))
    even_odd(num)
