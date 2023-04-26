'''
Write A Program To Get 6 Number In The TUPLE And Display All Number And Then Clear TUPLE And Then Display
'''

def Get_Numbers():
    list = []
    for i in range(6): # 0 1 2 3 4 5
        list.append(int(input("Enter 6 number : ")))
    return tuple(list)

if __name__=="__main__":
    print("This is the Tuple")
    tpl = Get_Numbers()
    print(tpl)
    tpl = list(tpl)
    tpl.clear()
    tpl = tuple(tpl)
    print("We have removed the tuple items")
    print(tpl)