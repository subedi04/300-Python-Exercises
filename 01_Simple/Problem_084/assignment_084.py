'''
Write A Python Program To Get Name From User, 
To Check It Is In Lowercase Or Not, 
If Not Lowercase Then Convert Into Lowercase
'''

if __name__=="__main__":
    name = input("Enter your name : ")

    if(name.islower()):
        print("Name is already in lowercase "+name)
    else:
        print("Lowercase name is converted to lowercase that is "+name.lower())