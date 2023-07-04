"""
Write A Python Program To Display 
All The Student Name Except Start 
With ‘f‘ And End With ‘n’ Char
"""
def Display_Name(std_list):
    for i in std_list:
        if(not(i.startswith('f') and i.endswith('n'))):
            print(i)

if __name__=="__main__":
    std_list = ['ali','kami','faisan','faiz','yash']
    print(std_list)
    Display_Name(std_list)