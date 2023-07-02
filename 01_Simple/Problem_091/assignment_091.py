'''
Write A Python Program Find A Mass Of An Object Through Density 
'''

if __name__=="__main__":
    density = int(input("Enter density of an object : "))
    volume = int(input("Enter volume of an object : "))
    # d = m / v, used to find density of an object

    mass = density / volume
    print("Mass = "+str(mass)+" gram")
    print("Volume = "+str(volume)+" cm3")
    print("Density = "+str(density)+" g/cm3")