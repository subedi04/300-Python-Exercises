'''
Write A Python Program To Get Age Of 10 Students 
From User And Store In A List. 
Condition Is That, System Should Display Age 
That Greater Than 14 Year And Less Than 20 Year
'''
# to get 10 std age
# store in list
# dispaly age greater than 14 and less than 20

if __name__=="__main__":
    std_age = []

    for i in range(0,10):
        std_age.append(int(input("Enter Age of student : ")))

    for i in std_age:
        if(i > 14 and i < 20):
            print(i)
