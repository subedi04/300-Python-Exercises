'''
Write A Program That Performs All Arithmetic Operations On Three Variables.
'''

print("#################################################")
print("##                                             ##")
print("##     ARITHMETIC OPERATIONS - 3 VARIABLES     ##")
print("##                                             ##")
print("#################################################")

print("\n>>> The operations are :\n")
print("\t Addition \t Substraction \t Multiplication\n\t Division \t Modulus\n")
print(">>> You must enter 3 numbers")

n1 = float(input("\tEnter number 1 : "))
n2 = float(input("\tEnter number 2 : "))
n3 = float(input("\tEnter number 3 : "))

print("\n>>> Results : ") 
print("\tOperation \t Answer\n")
print("\tAddition \t",n1+n2+n3)
print("\tSustraction \t", n1-n2-n3)
print("\tMultiplication \t", n1*n2*n3)
print("\tDivision \t", round(((n1/n2)/n3),2))
print("\tModulus \t", (n1%n2)%n3)