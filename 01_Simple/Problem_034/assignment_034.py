'''
Write A Python Program To Get 5 Color name From The User In List, 
Display That List, Remove First Color And Then Display All The Colors to User
'''

def get_colors():
    color_lst = []
    for i in range(5): # 0 1 2 3 4
        color_lst.append(input("Enter a color name : "))
    return color_lst
    
if __name__=="__main__":
    color_lst = get_colors()
    print("List color element "+str(color_lst))
    print("Total colors in the list = "+str(len(color_lst)))
    color_lst.pop(0)
    print("List color element "+str(color_lst))