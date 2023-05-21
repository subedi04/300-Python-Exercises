'''
Write A Python Program To Convert date to milliseconds 
'''
from datetime import datetime, timezone

def display_date(v):
    if(v == "yes"):
        return datetime.now()
    elif(v == "no") :
        return "Okay, we did not display date"
    else:
        return "Please enter value yes or no" 
 
def timestamp(dt):
    return dt.replace(tzinfo=timezone.utc).timestamp() * 1000
 
if __name__ == '__main__':
    val = input("Do you want to get date and time? (yes or no) :  ")
    dt = display_date(val)
    if val == "yes":
        print("Your date : "+ str(dt) + " in millisecinds is : " + str(timestamp(dt)))
    else:
        print(dt)
 