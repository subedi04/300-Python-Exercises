'''
Write A Python Program To get first and last name from the user 
and display full name. Make chaptalize both (First and last name)
'''

f_name = input("Enter your first name")
l_name = input("Enter your last name")

f_name = f_name.upper()
l_name = l_name.upper()
print("Your First name is "+ f_name)
print("Your Last name is "+l_name)
print("Your Full name is "+f_name +" "+ l_name)