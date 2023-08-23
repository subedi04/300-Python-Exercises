'''
Write a Python Program to get a number from user 
to check whether it is divisible by 5 or 
not using OOP.
'''


class Five:
	def getn(self):
		self.n = int(input("Enter a number : "))
    
	def show_result(self):
		if self.n%5 == 0:
			print(str(self.n)+" is divisible by 5")
		else:
			print("Not divisible by 5")

if __name__=="__main__":
	obj = Five()
	obj.getn()
	obj.show_result()
