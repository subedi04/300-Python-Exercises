'''
Write a Python Program to create a list on run time, 
display list element, and also find max and min item 
from list of integers using OOP.
'''
class MinMax:
    def getList(self):
        self.lst = []
        for i in range(5):
            self.item = int(input("Enter number"))
            self.lst.append(self.item)
    
    def showList(self):
        print(self.lst)
    
    def minmax(self):
        print("Max = "+str(max(self.lst)))
        print("Min = "+str(min(self.lst)))

if __name__=="__main__":
    obj = MinMax()
    obj.getList()
    obj.showList()
    obj.minmax()