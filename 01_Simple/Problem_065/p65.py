'''
Write A Python Program To Find Area And 
Perimeter Of A Square Using Function 
       (A = L2, P = 4a)
'''
# to get lenght of square

def area_peri(lenght):
    area = lenght*lenght
    perimeter = 4*lenght
    print("Area = "+str(area))
    print("Perimeter = "+str(perimeter))


if __name__ == "__main__":
    l = float(input("Enter lenght of square : "))
    area_peri(l)