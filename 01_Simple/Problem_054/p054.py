'''
Write A Python Program To Get A Number From The User 
To Find Factorial Of That Number
'''
# to get no
# find factorial 
# display result to user
import math

no = int(input("Enter a number to find its factorial : "))

fac_of_no = math.factorial(no)

print("Your number is "+str(no))
print("Factorial of "+str(no)+" is "+str(fac_of_no))
