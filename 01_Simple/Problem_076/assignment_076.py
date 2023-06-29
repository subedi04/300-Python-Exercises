'''
Write A Python Program Which Display 
Numbers That Are Divisible By 3 and 5 
From A List
'''
def Multiple_Three_Five():
    num_list = []
    for i in range(10):
        num_list.append(int(input("Enter list item : ")))
    
    for i in num_list:
        if(i%3==0 and i%5==0):
            print(i)

if __name__=="__main__":
    Multiple_Three_Five()
