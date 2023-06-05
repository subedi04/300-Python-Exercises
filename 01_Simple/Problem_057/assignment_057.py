'''
Write A Python Program To make binary to decimal conversion calculator 
'''

def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
 
 
# Driver code
if __name__ == '__main__':
    print("Binary to Decimal Calculator ")
    number = int(input("Enter your binary number : "))
    print("Your number at decimal is : ", binaryToDecimal(number))