"""
Write A Python Program To Take Age From The User To Check Whether User Able To Participate In Voting Or Not. 
If Age Is Less Than 18 Then It Don’t Allow To Participation. 
And Show, After How Much Year A Person Will Be Able To Participate:

Expected Result if user input 10 year then:
Sorry! You cannot participate in voting,
you will be able to participate after 8 year.
"""
name = input("Enter your name : ")
age = int(input("Enter your age : "))

if (age >= 18): 
    print("Hi " + name + " You can take part in votting.")
else : 
    print("Sory, you cannot take part because your age is " + str(age) + " years old")
    print("You will be abble to participate after " + str(18-age) + " years.")
