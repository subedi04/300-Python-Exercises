'''
PROBLEM 05:
Write A Program That Performs All Arithmetic Operations On Two Variables.
'''
print("#################################################")
print("##                                             ##")
print("##     ARITHMETIC OPERATIONS - 2 VARIABLES     ##")
print("##                                             ##")
print("#################################################")

print("\n>>> The operations are :\n")
print("\t Addition \t Substraction \t Multiplication\n\t Division \t Modulus\n")
print(">>> You must enter 2 numbers")

n1 = float(input("\tEnter number 1 : "))
n2 = float(input("\tEnter number 2 : "))

print("\n>>> Results : ") 
print("\tOperation \t Answer\n")
print("\tAddition \t",n1+n2)
print("\tSustraction \t", n1-n2)
print("\tMultiplication \t", n1*n2)
print("\tDivision \t", n1/n2)
print("\tModulus \t", n1%n2)