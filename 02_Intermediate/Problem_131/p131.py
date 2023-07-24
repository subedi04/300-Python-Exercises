'''
Write a Python Program to update any value in a dictionary on user request.
'''

if __name__=="__main__":
    d = {1:"Red",14:"Blue",2:"Yellow",6:"Black",9:"Green"}
    print(d)
    key = int(input("Enter a key, you want update : "))
    val = input("Enter a value : ")
    d[key] = val
    print(d)
