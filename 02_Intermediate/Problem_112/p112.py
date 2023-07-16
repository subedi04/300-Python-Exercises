'''
Write A Python Program To Find Gravitational Force
'''
# G =  6.6743 × 10^-11 = 0.00000000006674
# F = (G*(m1*m2))/r*r 

def Gravitational_Force(m1,m2,r):
    product = m1 * m2 
    G = 0.00000000006674
    Force = (G*(m1*m2))/r*r 
    print(str(Force)+" N")

if __name__=="__main__":
    m1 = float(input("Mass of object 1 : "))
    m2 = float(input("Mass of object 2 : "))
    r = float(input("Enter radius : "))

    Gravitational_Force(m1,m2,r)
