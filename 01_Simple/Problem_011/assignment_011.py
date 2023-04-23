'''
Write A Python Program To Get 3 Number From The User And Display Maximum Number
'''

def Max_3_numbers(n1,n2,n3):
    max = n1
    if max >n2 and max > n3 : 
        return max
    elif n2 > max and n2 > n3:
        max = n2
        return max
    elif n3 > max and n3 > n2 :
        max = n3
        return max
    else: 
        print("Equals Numbers")



if __name__=="__main__":
    print("Found the maximun of three numbers")
    n1 = float(input("Enter a number : "))
    n2 = float(input("Enter a number : "))
    n3 = float(input("Enter a number : "))
    print("The max number is : ", Max_3_numbers(n1,n2,n3))