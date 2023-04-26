'''
Write A Program That Performs All Compound Assignment Operations On An Integer
'''

# addition assignment operator
def addition(num):
    num += 5 # num + 5 -> 4 + 5 ->num
    print(num) # 9

# Subtraction assignment operator
def substraction(num):
    num -= 5 # num - 5 -> 4 - 5 ->num
    print(num) # 4

# Mulitplication assignment operator
def multiplication(num):
    num *= 5 # num * 5 -> 4 * 5 ->num
    print(num) # 20

# Division assignment operator
def division(num):
    num /= 5 # num / 5 -> 20 / 5 ->num
    print(num) # 4

# Mod assignment operator
def module(num):
    num %= 5 # num / 5 ->4 % 5 ->num
    print(num) # ?

if __name__=="__main__":
    num = int(input("Enter a integer : ")) #'4' -> 4
    addition(num)
    substraction(num)
    multiplication(num)
    division(num)
    module(num)
