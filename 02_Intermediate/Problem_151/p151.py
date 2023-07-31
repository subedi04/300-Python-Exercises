'''
Write a Python Program to Create a list from 
existed list that contain uppercase words
'''

if __name__=="__main__":
    lst = ["jafri","FAISAL","Zamir","ALI","JOHN","Green","PINK"]
    new_list = [i for i in lst if i.isupper()]
    print(new_list)