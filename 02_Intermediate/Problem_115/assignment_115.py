'''
Write a Python program to create a destructor.
'''

class MyClass:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        print(f"Object Information")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

    def __del__(self):
        print("\n")
        print(f"Destructor called for {self.name}")
        print(f"Destructor called for {self.age}")
        print(f"Object Deleted")


if __name__=="__main__":
    obj = MyClass("Miguel",26)
    del obj
