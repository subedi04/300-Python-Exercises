'''
Write A Python Program To Shuffle 
a List Of Different Color Code.
'''
# to get color code
# shuffle the color code and display

import random

def Shuffle_Color():
    color_code = []
    for i in range(5):
        color_code.append(input("Enter Color Code : "))
    random.shuffle(color_code)

    print(color_code)

if __name__=="__main__":
    Shuffle_Color()
