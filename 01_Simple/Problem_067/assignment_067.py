'''
Write A Python Program To Find Sum Of Two Number 
(1st Number Should Be Positive And 2nd Number 
Should Be Negative And Less Than 50 And Greater Than 20)
'''
def find_sum():
    while True:
        positive_num = int(input("Enter a positive number: "))
        if positive_num <= 0:
            print("Invalid input! Please enter a positive number.")
        else:
            break

    while True:
        negative_num = int(input("Enter a negative number (-50 to -20): "))
        if negative_num >= 0 or negative_num > -20 or negative_num < -50:
            print("Invalid input! Please enter a negative number between -50 and -20.")
        else:
            break

    sum_of_numbers = positive_num + negative_num
    print(f"The sum of {positive_num} and {negative_num} is: {sum_of_numbers}")

if __name__=="__main__":
    find_sum()
