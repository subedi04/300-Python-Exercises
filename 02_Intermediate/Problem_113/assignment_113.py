'''
Write A Python Program To Get a length in cm and convert to m and km
'''

def convert_cm_to_m_km(length_cm):
    length_m = length_cm / 100
    length_km = length_cm / 100000
    return length_m, length_km


if __name__=="__main__":
    length_cm = float(input("Enter length in centimeters: "))

    length_meters, length_kilometers = convert_cm_to_m_km(length_cm)

    print("Length in meters:", length_meters, "m")
    print("Length in kilometers:", length_kilometers, "km")
