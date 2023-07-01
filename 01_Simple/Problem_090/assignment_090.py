'''
Write A Python Program To Get Name Of 
Different Students From User And Store In A List. 
Condition Is That, System Should Display The Name Of 
Student That Start From Char ‘a’ And End At ‘a’ Char 
'''

if __name__=="__main__":
    list_name = []

    for i in range(0,10):
        list_name.append(input("Enter Name of Student : "))

    for i in list_name:
        if(i.startswith('a') and i.endswith('a')):
            print(i)
