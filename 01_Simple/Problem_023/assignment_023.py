''''
Write a Python program get name of week and show “Holiday” if user input Sunday or Friday
'''

def holyday_sun(week_name):
    if(week_name == 'Sunday' or week_name == 'Sun' or week_name == 'sun'or  week_name == 'sunday' ):
        print("It is holiday")
    elif (week_name == 'Friday' or week_name == 'Fri' or week_name == 'fri'or  week_name == 'friday'):
        print("It is holiday")
    else:
        print("It is not Holiday")


if __name__=="__main__":
    week_name  = input("Enter a week name :  ")
    holyday_sun(week_name)
