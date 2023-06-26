'''
Write A Python Program 
To Clone Or Copy Of a 
10 Color List.
'''
# to get 10 color
# copy of color list
# Display both list

def get_Colors():
    color_list = []
    for i in range(10):
        color_list.append(input("Enter color name : "))
    return color_list

if __name__=="__main__":
    color_list = get_Colors()
    print("Orignal List = "+str(color_list))

    new_color_list = color_list.copy()
    new_color_list.pop()
    print("Copied List = "+str(new_color_list))
