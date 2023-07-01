"""
Write A Python Program To Get Name From A List, That Start with ‘n'
"""

def Name_Start_N(person_name):
    print("Names starts with 'n' : ")
    for i in person_name:
        if(i.startswith('n') or i.startswith('N')):
            print(i)


if __name__=="__main__":
        
    person_name = ['Ali','Nami','faisal','faiz','ahmad','natir','Nadal']
    print("List of names : ",person_name)
    Name_Start_N(person_name)