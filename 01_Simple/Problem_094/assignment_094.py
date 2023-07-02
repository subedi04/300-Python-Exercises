'''
Write Python Program To Find Mass 
Of A Object That Accelerated By Man
'''

def Mass(force,acc):
    mass = force/acc
    print("Mass of a object = "+str(mass)+" kg")
    print("Acceleration of a object = "+str(acc)+" m/s2")
    print("Force of a man = "+str(force)+" N")

if __name__=="__main__":
    force = float(input("Enter force of an object in N : "))
    acc = float(input("Enter acc of an object in m/s2 : "))
    # F = ma
    Mass(force,acc)