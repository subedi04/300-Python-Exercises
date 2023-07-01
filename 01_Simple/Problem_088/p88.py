'''
Write A Python Program To Get A Number From User, 
The System Should Add Auto Increment To That Number. 
Half Of User Entered Number Should Be Incremented 
'''
# to get number
# find half of that number
# add to user entered number
if __name__=="__main__":
    num = int(input("Enter a number : "))
    # find half of that number
    half_num = num/2
    print("Half of "+str(num)+ "is "+str(half_num))
    add = num + half_num
    print("Result is "+str(add))