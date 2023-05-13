'''
Write A Python Program To Get 5 Color name From The User In List, 
Display That List, Remove Last Color And Then Display All The Colors to User
'''
# get 5 color from the user
# display color
# rm last color
# display

def get_colors():
    color_lst = []
    for i in range(5): # 0 1 2 3 4
        color_lst.append(input("Enter a color name : "))
    return color_lst
    

if __name__=="__main__":
    color_lst = get_colors()
    print("List color element "+str(color_lst))
    color_lst.pop()
    print("List color element "+str(color_lst))

