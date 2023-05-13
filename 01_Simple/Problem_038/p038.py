'''
Write A Python Program To Convert Radian To Degree 
'''
# to get radian 
# convert to degree
import math
if __name__=="__main__":
    rad = int(input("Enter angle in radian"))
    deg = math.degrees(rad)
    print("Your radian "+str(rad)+" is Converted to degree that is "+str(deg))