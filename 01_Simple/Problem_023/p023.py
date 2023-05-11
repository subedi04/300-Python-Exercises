'''
Write a Python program get name of week and show “Holiday” if user input Sunday
'''
# to get week name
# sunday, then display it is holiday

def holyday_sun(week_name):
    if(week_name == 'Sunday' or week_name == 'Sun' or week_name == 'sun'or  week_name == 'sunday' ):
        print("It is holiday")
    else:
        print("It is not Holiday")


if __name__=="__main__":
    week_name  = input("Enter a week name :  ")
    holyday_sun(week_name)

