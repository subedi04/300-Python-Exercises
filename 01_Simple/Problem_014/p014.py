'''
Write A Program To Get 6 Number In The List And Sum That Number
'''

def Get_Numbers():
    lst = []
    for i in range(6): # 0 1 2 3 4 5
        lst.append(int(input("Enter 6 number : ")))
    return lst


def Sum_List(lst):
    s = 0
    for i in lst:
        s += i
    return s
    #print("Sum of number in the list "+str(s))

if __name__=="__main__":
    lst = Get_Numbers()
    print("Sum of number in the list =  "+str(Sum_List(lst)))