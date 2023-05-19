'''
Write A Python Program To Get Second And Then Convert Second To Hours 
'''

def second_to_hours(s):
    hours = s/3600
    return round(hours,1)

if __name__=="__main__":
    s = float(input("Enter seconds to convert to hours : "))
    h = second_to_hours(s)
    print("You entered "+str(s)+" s")
    print(str(s)+" seconds is converted to hours that is "+str(h)+" H")