"""
Write A Python Program To Check A Year,
 Whether It Is Leap Year Or Not
"""
# to get year 
# check, leap or not

def Leap_Year(year):
    if(year%4 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

if __name__=="__main__":
    year = int(input("Enter a year : "))
    Leap_Year(year)

