'''
Write A Python Program To Get 2 Number From The User 
Store In Variable, Swap That Number And Then Display The New Value Of Both.
'''
# to get 2 numebr from the user
# store in the variables
# swaping their values
def swap(n1,n2):
    temp = n1
    n1 = n2
    n2 = temp
    return n1,n2

if __name__=="__main__":
    a = input("Enter A value : ")# 5
    b = input("Enter B value : ")# 4

    print("Values before swaping")
    print("a = "+str(a))
    print("b = "+str(b))

    print("Values After swaping")
    a,b = swap(a,b)
    
    print("a = "+str(a))
    print("b = "+str(b))


