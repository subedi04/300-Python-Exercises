'''
Write a Python Program To Append Those Number That Are 
Divisible By 5 And 7 From a Range (10, 100) 
To A New Created List.
'''
if __name__=="__main__":
    lst = []
    for i in range(10,101):
        if i%5 == 0 and i%7 == 0:
            lst.append(i)

    print(lst)