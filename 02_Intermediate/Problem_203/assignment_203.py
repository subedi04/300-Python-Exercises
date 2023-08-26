'''
Write a Python Program to find addition 
of list element to create a new list. 
Add element of list as 1st and 2nd….  
Using OOP.
'''

class ListAddition:
    def __init__(self):
        self.input_list = []
        self.result_list = []

    def input_numbers(self):
        try:
            n = int(input("Enter the number of elements in the list: "))
            for i in range(n):
                num = float(input(f"Enter element {i + 1}: "))
                self.input_list.append(num)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    def calculate_result(self):
        total = 0
        for num in self.input_list:
            total += num
            self.result_list.append(total)

    def display_result(self):
        print("Original List:", self.input_list)
        print("Result List:", self.result_list)

def main():
    list_addition = ListAddition()
    list_addition.input_numbers()
    list_addition.calculate_result()
    list_addition.display_result()

if __name__ == "__main__":
    main()
