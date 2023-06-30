"""
Write A Python Program To Get Name From A List, That End at ‘f'
"""

def Names_End_F(names):
    print("Names starts with 'f' : ")
    for i in names:
        if(i.endswith('f')):
            print(i)

if __name__=="__main__":
    person_name = ['Alif','kami','faisal','faif','ahmaf','fatir','ray']
    print("List of names : ",person_name)
    Names_End_F(person_name)

