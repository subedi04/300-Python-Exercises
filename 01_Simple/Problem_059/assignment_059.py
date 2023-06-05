'''
Write A Python Program To Get A Bio From A User 
And Count Specific word in a User Bio.
'''

user_bio = input("Enter your Bio : ")
print("Your bio is \n")
print(user_bio)

user_bio_list =  user_bio.split()
print("Total words = "+str(len(user_bio_list)))