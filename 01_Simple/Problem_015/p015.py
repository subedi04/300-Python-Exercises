'''
Write A Program To Get 6 Number In The List And Display All Number And Then Clear List And Then Display
'''
# get six number from the user
# display 
# clear list
# then display

def Get_Numbers():
    lst = []
    for i in range(6): # 0 1 2 3 4 5
        lst.append(int(input("Enter 6 number : ")))
    return lst


if __name__=="__main__":
    print("This is the list")
    lst = Get_Numbers()
    print(lst)
    lst.clear()
    print("We have removed the list items")
    print(lst)


