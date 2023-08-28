from math import sqrt

a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))

r = b*b-4*a*c

if r > 0:
    x1 = (-b + sqrt(r))/2*a
    x2 = (-b - sqrt(r))/2*a
    print(x1,x2)
    print("There are two roots")
elif r == 0:
    x = -b/2*a
    print("There is one root")
else:
    print("No roots")