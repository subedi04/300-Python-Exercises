'''
Write a Python Program to count number of instances 
of a Python class. Use another Method.
'''

class MyClass:
    instances = 0  
    
    def __init__(self):
        MyClass.instances += 1
        
    @classmethod
    def get_instance_count(cls):
        return cls.instances

if __name__=="__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    obj3 = MyClass()

    instance_count = MyClass.get_instance_count()

    print("Number of instances:", instance_count)
