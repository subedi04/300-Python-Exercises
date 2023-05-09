# get 5 number from the user
# store in the array and display 
# find max

import array as arr

def enter_data():
    a = arr.array('i',[])
    for i in range(5):#0 to 4 
        a.append(int(input("Enter a number to store in the array : ")))
    return a

def maximun(a):
    m = a[0] # 2,3,4,5,6
    for j in range(5):
        print(a[j])
        if(a[j] > m):
            m = a[j]
    print("Max Number = "+str(m))

if __name__=="__main__":
    a = enter_data()
    maximun(a)

