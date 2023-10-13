'''
Write a Python Program to read any specific line from a file.
'''

if __name__=="__main__":
    file = open("input.txt","r")
    r = file.readlines()
    line = int(input("Enter a line number : ")) # 1
    print(r[line-1]) 