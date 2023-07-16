'''
Write a Python program to create a parameterized 
and non parameterized constructor.
'''
# class Jafri:
#     def __init__(self):
#         print("This is the non parameterized Constructor...")
    
# obj = Jafri()

class Jafri:
    def __init__(self,name, user_id):
        self.name = name
        self.user_id = user_id
        print(self.name)
        print(self.user_id)


if __name__=="__main__":
    obj = Jafri("Jafri",22)
