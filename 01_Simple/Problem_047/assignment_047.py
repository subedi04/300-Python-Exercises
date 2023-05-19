'''
Write A Python Program To Get 2 Number From The User, 
Find Their Cube, And Add Both Result, 
Finally Result Display To User.
'''

def cube(n):
    cube = 1
    flag = 3

    while(flag > 0):
        cube = cube * n
        flag -= 1
    return cube

def Addition(n1,n2):
    return n1+n2

if __name__=="__main__":
    n1 = int(input("Enter 1st number : "))
    n2 = int(input("Enter 2nd number : "))

    n1_c = cube(n1)
    n2_c = cube(n2)

    print("Cube of 1st numebr is "+str(n1_c))
    print("Cube of 2nd numebr is "+str(n2_c))
    add_c = Addition(n1_c,n2_c)
    
    print("Addition of both Cube is "+str(add_c))
