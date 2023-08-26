'''
Write a Python Program to get a number from user to check 
whether it is multiple of 2 and 3 or not using Procedural 
programming.
'''
def main():
    try:
        number = int(input("Enter a number: "))
        
        if number % 2 == 0 and number % 3 == 0:
            print(f"{number} is a multiple of both 2 and 3.")
        else:
            print(f"{number} is not a multiple of both 2 and 3.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


