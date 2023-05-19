'''
Write A Python Program To Get Hours 
And Then Convert Hours To Second
'''
# to get hours
# convert to second

def hours_to_seconds(h):
    return h*3600

if __name__=="__main__":
    h = float(input("Enter hours to convert to second : "))
    s = hours_to_seconds(h)
    print("You entered "+str(h)+"H")
    print(str(h)+" hour(s) is converted to second that is "+str(s)+" s")