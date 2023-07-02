"""
Write A Python Program To Find Time Taken By An Object 
Having Velocity difference ‘dv‘ And ‘a’ Acceleration. 
Get Velocity And Acceleration From The User
'''
"""

def Time(vi,vf,a):
    change_velocity = vf-vi
    t = change_velocity / a
    print("Time of an obejct = "+str(t)+"m/s2")

if __name__=="__main__":
    vi = float(input("Enter vi in m/s : "))
    vf = float(input("Enter vf in m/s : "))
    a = float(input("Enter acceleration in m/s2 : "))
    Time(vi,vf,a)