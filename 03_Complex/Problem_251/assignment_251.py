'''
Write a Python Program to create an class with data members.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


if __name__=="__main__":

    emp1 = Employee("John", 20000)
    emp1.display()
