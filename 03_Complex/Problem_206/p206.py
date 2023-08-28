'''
Write A Python Program To Generate Random Number, 
And Display Message If Required Number Matched. 
Required Number Will Be Taken From User
'''

import random
# get start, end, message, req_num
# s = int(input("Enter a start number"))
# e = int(input("Enter a end number"))
# msg = input("Enter a message")

if __name__=="__main__":
    req_number = int(input("Enter a number to match : "))

    gen_n = random.randint(0,10)

    if gen_n == req_number:
        print("number is matched...")
    else:
        print("Number did not match..")

