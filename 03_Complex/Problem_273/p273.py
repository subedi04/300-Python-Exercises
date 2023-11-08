'''
Write a Python Program to take a string from user to search in a file
'''

para = input("Enter a paragraph : ")
# I am faisal zamir, working on teaching programming languages, web designing, web development everything...
file = open("mysearchfile.txt","r+")

word = input("Enter a word to search in file : ")
lines = file.readlines()
for line in lines:
    if line.find(word) != -1:
        print("Word is existed")
    else:
        print("No word is there")
file.write(para)
file.close()

