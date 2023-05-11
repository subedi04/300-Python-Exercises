'''
Write A Python Program To Get 5 Year From The User 
To Store In Array And Display Only Leap Year To User
'''
import array as arr

def enter_data():
    vector = arr.array('i',[])
    for i in range(5):#0 to 4 
        vector.append(int(input("Enter a number to store in the array : ")))
    return vector

def Leap_Year(vector):
    for year in vector:
        if(year%4 == 0):
            print(year, " Leap Year")

if __name__=="__main__":
    vector = enter_data()
    print("\n")
    Leap_Year(vector)
