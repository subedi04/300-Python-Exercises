'''
Write Python Program To Get Username From User And 
Make Sure That Username Should Contain Alphanumeric Character 
AND Username Length Should Not Be Less Than Or Equal To 8 
'''


def check_user(u):
    if(u.isalnum() and len(u)>8):
        print("Your Username "+str(u)+" is Okay")
    else:
        print("Sorry, use only alpha or numaric without whitespace and the size should be greather to 8")

if __name__=="__main__":
    user = input("Enter username :  ")
    check_user(user)