'''
Write a Python Program To Find Roots Of 
Quadratic Equation: Make some modification
'''

import math

def quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None  # No real roots

# Get coefficients from the user
try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    # Calculate roots using the function
    roots = quadratic_roots(a, b, c)
    
    # Display the roots
    if roots is None:
        print("The quadratic equation has no real roots.")
    elif len(roots) == 2:
        root1, root2 = roots
        print(f"The roots are: {root1} and {root2}")
    else:
        root = roots[0]
        print(f"The root is: {root}")

except ValueError:
    print("Invalid input. Please enter numerical coefficients.")
