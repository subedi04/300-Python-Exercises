'''
Write A Python Program To Get Password From 
The User That Contain Alpha Numeric And More 
Than 8 And Less Than 20 Characters
'''
# to get pwd
# check alpha num, 
# char more 8 and less than 20

if __name__=="__main__":
    pwd = input("Enter your password")# 3483803

    if(pwd.isalnum() and not pwd.isalpha() and not pwd.isdigit()):
        if(len(pwd) > 8 and len(pwd) < 20):
            print("Your password is okay")
        else:
            print("Sorry, your password is not correct, you have to enter pwd, that should be more than 8 and less than 20 char")
    else:
        print("Sorry, include alpha and numaric in your password")