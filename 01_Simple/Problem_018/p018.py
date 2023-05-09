# to store user info
# then display
# then update record
# then display
# key:value, name:xyz
'''
Write A Python Program to store name, address, contact in dictionary, and then update his/her contact number 
'''

user_info = {"name":"Ali","address":"DIKHAN","contact":891828932}
print("First Record")
print(user_info)
user_info.update({"contact":1233445})
print("Updated Record")
print(user_info)
