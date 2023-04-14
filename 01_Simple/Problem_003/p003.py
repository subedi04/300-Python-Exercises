'''
Write A Program To Get Name And Age From The User And Display Name And Age On The Screen In This Format:

Expected Result if name is “Faisal Zamir” and age is 25 then:
Hi Faisal Zamir! Your age is 25.
'''

name = input("Enter Name : ")
age = int(input("Enter input : "))

print("Hi "+ name + "! Your age is " + str(age))