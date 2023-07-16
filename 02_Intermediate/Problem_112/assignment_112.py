'''
Write A Python Program To Find Coulomb Force between two charges.
'''

def Coulomb_Force(q1, q2, r):
    k = 9 * 10**9  # electrostatic constant in Nm^2/C^2
    force = (k * abs(q1 * q2)) / (r**2)
    return force

# Example usage
if __name__=="__main__":
    #q1 = 2.5e-6  # charge 1 in C
    #q2 = 3e-6    # charge 2 in C
    #r = 0.1      # distance in meters
    q1 = float(input("Enter charge q1 : "))
    q2 = float(input("Enter charge q2 : "))
    r  = float(input("Enter distance in meters : "))
    coulomb_force = Coulomb_Force(q1, q2, r)
    print("Coulomb force:", coulomb_force, " N")
