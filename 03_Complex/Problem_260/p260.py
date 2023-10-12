'''
Write a Python Program to Read content from one file 
and write it into another file.
'''

input = open("input.txt","r")
output = open("output.txt","w")

for line in input:
    output.write(line)

input.close()
output.close()