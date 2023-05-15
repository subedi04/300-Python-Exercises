'''
Write A Python Program To Get A Angle From The User 
And Find Its Sin And Cos Value In Radian 
And Then Convert Their Result Into Degree Unit
'''
import math

if __name__=="__main__":

    angle = float(input("Enter a angle : "))

    sin_value = math.degrees(math.sin(angle))# in the radian --> degrees
    cos_value = math.degrees(math.cos(angle)) # in the radian

    print("Sin Value = "+str(sin_value)+" degrees")
    print("Cos Value = "+str(cos_value)+" degrees")