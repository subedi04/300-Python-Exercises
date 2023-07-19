'''
Write a Python program to count total number of lists in a nested list.
'''
def Num_of_List(ne_list):
    list_total = 0
    for i in ne_list:
        if type(i) == list:
            list_total += 1
    print(list_total)

if __name__=="__main__":
    ne_list = [1,2,3,[2,2],["Jafri","Faisal"],[1.2,0.4]]
    Num_of_List(ne_list)

