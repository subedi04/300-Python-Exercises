'''
Write A Python Program To Get Name From User, 
To Check It Is In Uppercase Or Not, If Not Upper 
Then Convert Into Uppercase
'''
# to get name
# convert to uppercase if not
# display to user

if __name__=="__main__":
    name = input("Enter your name : ")

    if(name.isupper()):
        print("Name is already in uppercase "+name)
    else:
        print("Lowercase name is converted to uppercase that is "+name.upper())