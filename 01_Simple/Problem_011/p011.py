'''
Write A Python Program To Get 2 Number From The User And Display Maximum Number
'''

def max_two_numbers(n1,n2):
    if n1 > n2:  
        return n1
    return n2

if __name__=="__main__":
    print("Found the maximun of two numbers")
    n1 = float(input("Enter a number : "))
    n2 = float(input("Enter a number : "))
    print("The max number is : ", max_two_numbers(n1,n2))