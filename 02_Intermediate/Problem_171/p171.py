'''
Write a Python Program to count number 
of instances of a Python class.
'''

class Jafri:
    x = 0
    def __init__(self):
        Jafri.x += 1
    
obj = Jafri()
obj = Jafri()
obj = Jafri()
obj = Jafri()
obj = Jafri()
obj = Jafri()
obj = Jafri()

if __name__=="__main__":
    print(Jafri.x)