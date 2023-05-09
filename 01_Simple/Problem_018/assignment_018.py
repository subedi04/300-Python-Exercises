# to store user info
# then display
# then update record
# then display
# key:value, name:xyz
'''
Write A Python Program to store name, address, contact in dictionary, 
and then update user contact number,  but user will enter 
his/her contact number at run time
'''

user_info = {"name":"Ali","address":"DIKHAN","contact":891828932,"user_contact_number":19777}
print("First Record")
print(user_info)
user_info.update({"user_contact_number":20888})
print("Updated Record")
print(user_info)
