'''
Write A Python Program To Get A Number From The User 
To Find Factorial Of That Number. 
Using another method as I discussed
'''

def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n*factorial(n-1)
    
if __name__=="__main__":
    no = int(input("Enter a number to find its factorial : "))
    fac_of_no = factorial(no)
    print("Your number is "+str(no))
    print("Factorial of "+str(no)+" is "+str(fac_of_no))
