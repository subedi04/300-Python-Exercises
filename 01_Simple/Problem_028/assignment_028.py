'''
Write A Python Program To Get A Number 
From User To Find Cube Of That Number
'''

def Cube_Number(n):
    return pow(n,3)

if __name__== "__main__":
    n = float(input("Enter a number : "))
    cube = Cube_Number(n)
    print("The cube of " + str(n) + " is : " + str(cube) )