'''
Write A Python Program To Get a Angle From The User 
And Find Its Sin And Cos Value In Radian
'''
# get angle from the user
# find cos and sin value in radian 

import math

if __name__=="__main__":

    angle = float(input("Enter a angle : "))

    sin_value = math.sin(angle) # in the radian
    cos_value = math.cos(angle) # in the radian

    print("Sin Value = "+str(sin_value)+"rad")
    print("Cos Value = "+str(cos_value)+"rad")
