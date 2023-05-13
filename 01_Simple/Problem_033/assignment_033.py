'''
Write A Python Program To Get Element From The User, 
Store In The List, And Count That Element And 
Display Result To User
'''
import array as arr

def enter_data():
    v = arr.array('i',[])
    for i in range(5):#0 to 4 
        v.append(int(input("Enter a element : ")))
    return v

if __name__=="__main__":
    v = enter_data()
    print("Element in the list = "+str(v))
    print("Total elements in the list = "+str(len(v)))