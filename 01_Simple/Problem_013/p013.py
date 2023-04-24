'''
Write Python Program To Get Password From User And Make Sure That Password Should Contain Number And Alphabetic
'''

def Check_Password(pwd):
    if(pwd.isalnum()):
        print("Your password is okay, that is "+pwd)
    else:
        print("Sorry, we did not allow white space and special char in your password that is "+pwd)


if __name__=="__main__":
    pwd = input("Enter your password : ")
    Check_Password(pwd)
