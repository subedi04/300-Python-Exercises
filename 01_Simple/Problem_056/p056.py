'''
Write A Python Program To  Make a percentage calculator. 
'''
# get amount
# cal per from that amount

def Percent(amount,per):
    return (per*amount)/100

if __name__=="__main__":
    amount = int(input("Enter amount : ")) #100
    per = int(input("Enter percentage, you wan to get : ")) # 20

    percentage = Percent(amount,per)

    print("Your amount is = "+str(amount))
    print("Your percentage from "+str(amount)+ " is "+str(percentage))
