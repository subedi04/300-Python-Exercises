'''
Write A Python Program To 
Add Number From List That 
Are Greater Than 5 And 
Less Than 10
'''
# create a list, store items number
# add >5, 10<
if __name__=="__main__":
    lst = [1,3,1.3,5,10,7,7,4,8,9,50,43] # 7+8+9 = 24
    s = 0
    for i in lst:
        if(i > 5 and i < 10):   
            s += i
    print(s)