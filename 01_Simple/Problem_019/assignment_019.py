'''
Write A Python Program To Get 4 Number From User 
And Put In The Following Equation:

d+a+2ab/d(4c+10)
'''

def equation(a,b,c,d):
 	result = (d+a+(2a*b))/(d*(4*c+10))
 	return result
 	

if __name__=="__main__":

	a = int(input("Enter a number : "))
	b = int(input("Enter b number : "))
	c = int(input("Enter c number : "))
	d = int(input("Enter d number : "))
	
	result = equation(a,b,c,d)
	print("Result is = "+str(result))
	
