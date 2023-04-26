'''
Write A Program That Performs All Compound Assignment Operations On An Integer. \
And Add All The Result, And Then Display To User.
'''
# addition assignment operator
def addition(num):
    num += 5 # num + 5 -> 4 + 5 ->num
    return num

# Subtraction assignment operator
def substraction(num):
    num -= 5 # num - 5 -> 4 - 5 ->num
    return num

# Mulitplication assignment operator
def multiplication(num):
    num *= 5 # num * 5 -> 4 * 5 ->num
    return num

# Division assignment operator
def division(num):
    num /= 5 # num / 5 -> 20 / 5 ->num
    return num

# Mod assignment operator
def module(num):
    num %= 5 # num / 5 ->4 % 5 ->num
    return num

def Results(num):
    print("The results are : ")
    print("Addition \t", addition(num))
    print("Substraction \t", substraction(num))
    print("Multiplication \t", multiplication(num))
    print("Divsion \t",division(num))
    print("Module \t", module(num))

if __name__=="__main__":
    num = int(input("Enter a integer : ")) #'4' -> 4
    Results(num)