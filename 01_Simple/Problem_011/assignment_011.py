'''
Write A Python Program To Get 3 Number From The User And Display Maximum Number
'''

def Max_3_numbers(n1,n2,n3):
    max = n1
    if n2>max:
        max = n2
    if n3 > max:
        max = n3
    if max==n1 and max ==n2: 
        print("Equals Numbers")
    return max

if __name__=="__main__":
    print("Found the maximun of three numbers")
    
    n1 = float(input("Enter a number : "))
    n2 = float(input("Enter a number : "))
    n3 = float(input("Enter a number : "))
    
    print("The max number is : ", Max_3_numbers(n1,n2,n3))
