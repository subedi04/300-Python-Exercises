'''
Write A Python Program To Convert Degree To Radian 
'''
import math
if __name__=="__main__":
    deg = int(input("Enter angle in degrees : "))
    rad = math.radians(deg)
    print("Your degree "+str(deg)+" is Converted to radians that is "+str(rad))