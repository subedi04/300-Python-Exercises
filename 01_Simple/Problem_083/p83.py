"""
Write A Python Program To Get Name From A List, That Start From ‘f'
"""
# to create list
# store person name / color name / std name 
# to display person name that start from f char

def Name_Start_F(person_name):
    print("Names starts with 'f' : ")
    for i in person_name:
        if(i.startswith('f')):
            print(i)


if __name__=="__main__":
        
    person_name = ['Ali','kami','faisal','faiz','ahmad','fatir','ray']
    print("List of names : ",person_name)
    Name_Start_F(person_name)