'''
Write A Python Program To Get a length in mm and convert to m and km
'''

if __name__=="__main__":
    mm = float(input("Enter a length in mm : "))
    # 1mm = 0.001 m
    # 1mm = 0.000001 km

    m = mm * 0.001
    km = mm * 0.000001

    print("Milimeter "+str(mm)+" is converted into " +str(m)+" meters")
    print("Milimeter "+str(mm)+" is converted into " +str(km)+" kilo meters")