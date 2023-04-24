'''
Write  Python Program To Get Password From User And Make Sure 
That Password Should Contain Number And Alphabetic AND 
Password Length Should Not Be Greater Than Or Equal To 8
'''

def Check_Password(pwd):
    size_pwd = len(pwd)
    if(pwd.isalnum() ):
        print("Your password is okay, that is "+pwd)
    else:
        print("Sorry, we did not allow white space and special char in your password that is "+pwd)

    if size_pwd <= 8 :
        print("The size of your password is OK!!! ")
    else:
        print("The size of your password is : ", size_pwd)
    
if __name__=="__main__":
    pwd = input("Enter your pasword : ")
    Check_Password(pwd)