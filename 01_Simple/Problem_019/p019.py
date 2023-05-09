# to get 3 num from user
# put in to the equaiton 
# dispaly result to user

'''
Write A Python Program To Get 3 Number From User And 
Put In The Following Equation:

	a+b+ca/b(2a + 3b)
'''

def equation(a,b,c):
	result = (a+b+c)*(a/b)*(2*a+3*b)
	return result

if __name__=="__main__":

	a = int(input("Enter a number : "))
	b = int(input("Enter b number : "))
	c = int(input("Enter c number : "))

	result = equation(a,b,c)
	print("Result is = "+str(result))
