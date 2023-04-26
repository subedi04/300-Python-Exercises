'''
Write a program to get 6 number in the TUPLE and sum that number
'''

def Get_Numbers():
    list = []
    for i in range(6): # 0 1 2 3 4 5
        list.append(int(input("Enter 6 number : ")))
    return tuple(list)


def Sum_List(tuple):
    return sum([i for i in tuple])

if __name__=="__main__":
    tuple = Get_Numbers()
    print(tuple)
    print("Sum of number in the tuple =  "+str(Sum_List(tuple)))