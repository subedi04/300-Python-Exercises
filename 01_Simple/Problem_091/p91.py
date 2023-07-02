'''
Write A Python Program Find A Density Of An Object
'''
# to get mass, volume of an object
# find density of an object
if __name__=="__main__":
    mass = int(input("Enter mass of an object : "))
    volume = int(input("Enter volume of an object : "))
    # d = m / v, used to find density of an object

    density = mass / volume
    print("Mass = "+str(mass)+" gram")
    print("Volume = "+str(volume)+" cm3")
    print("Density = "+str(density)+" g/cm3")