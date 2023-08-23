'''
Write a Python Program to get a number from user 
to check whether it is multiple of 5 or not using 
Procedural programming.
'''

def is_multiple_of_5(number):
	if number % 5 == 0:
		return True
	else:
		return False


if __name__=="__main__":
	user_input = input("Enter a number: ")

	try:
		number = int(user_input)
		if is_multiple_of_5(number):
			print(f"{number} is a multiple of 5.")
		else:
			print(f"{number} is not a multiple of 5.")
		except ValueError:
		  print("Invalid input. Please enter a valid number.")

