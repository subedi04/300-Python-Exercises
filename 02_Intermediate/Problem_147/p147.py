'''
Write Python Program to make use of isidentifier method with string
'''
if __name__=="__main__":
    identifier = input("Enter a identifier : ")

    if identifier.isidentifier():
        print("This is valid identifier")
    else:
        print("Not a valid")