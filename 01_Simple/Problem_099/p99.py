'''
Write A Python Program To Get Only 
Uppercase Words From User To Store 
in A List 
'''
# to get 10  words from user
# uppercase
if __name__=="__main__":
    lst = []
    for i in range(10): # 0 to 9
        w = input("Enter word to store in list : ")
        if(w.isupper()):
            lst.append(w)
        else:
            print("Error! Insert Uppercase word : ")
    print(lst)
