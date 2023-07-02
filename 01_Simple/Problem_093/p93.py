'''
Write A Python Program To Find Acceleration 
Of An Object Having Velocity v in t Time. 
'''
# to get change in velocity
# get time in s
# find acc
def Acceleration(vi,vf,t):
    change_velocity = vf-vi
    acc = change_velocity / t
    print("Acceleration of an obejct = "+str(acc)+"m/s2")

if __name__=="__main__":
    vi = float(input("Enter vi in m/s"))
    vf = float(input("Enter vf in m/s"))
    t = float(input("Enter time in s"))
    Acceleration(vi,vf,t)