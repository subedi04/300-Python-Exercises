'''
Write A Python Program That Accepts Six Identity Numbers Of Students, 
Clear The List Item And Make Use Of Empty Method To Check, 
It Has Been Empty Or Not
'''

def clear_list():
    identity_numbers = []

    for i in range(6):
        identity_number = input("Enter an identity number: ")
        identity_numbers.append(identity_number)

    print("List before clearing:", identity_numbers)

    identity_numbers.clear()

    if identity_numbers:
        print("List is not empty.")
    else:
        print("List is empty.")

if __name__=="__main__":
    clear_list()
