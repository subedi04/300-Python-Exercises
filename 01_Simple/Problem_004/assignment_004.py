"""
Write A Python Program To Take Marks From The User To Check Whether User Able To Admission In College Or Not. 
If Marks Is Less Than 60 Then It Don’t Allow To Take Admission. 

Expected Result if user input 50 year then:
Sorry! You cannot take admission, you need 10 numbers more to take admission.
"""

print("#############################################################")
print("##                                                         ##")
print("##                        ADMISION                         ##")
print("##                                                         ##")
print("#############################################################")

mark = float(input("Enter your Mark : "))

if (mark < 60):
    print("Sorry! You cannot take admission, you need " + str(int(60-mark)) + " numbers more to take admission.")
elif (mark == 100) :
    print("PERFECT!!! You are accepted with 100 points")
else:
    print("Congratulations!!! You are accepted")