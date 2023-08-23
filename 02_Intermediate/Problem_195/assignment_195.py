'''
Write a Python Program to display odd number from array using OOP.
'''

class OddNumberDisplay:
    def __init__(self, num_list):
        self.num_list = num_list

    def display_odd_numbers(self):
        print("Odd Numbers:")
        for num in self.num_list:
            if num % 2 != 0:
                print(num)

if __name__=="__main__":
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	odd_number_display = OddNumberDisplay(numbers)

	odd_number_display.display_odd_numbers()

