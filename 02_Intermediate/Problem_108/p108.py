''''
Write a Python Program To Update Specific Key In A Dictionary.
'''
if __name__=="__main__":
    dict = {"Name":"Faisal","Age":30,"cors":"Python"}
    print(dict)
    old_key = input("Enter a key you want to update : ")
    new_key = input("Enter a new : ")
    dict[new_key]  = dict[old_key]
    del dict[old_key]
    print(dict)