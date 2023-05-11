'''
Write A Python Program To Get Student Marks , 
If Marks Is Less Than 40, It Display “Fail” Otherwise “Pass”.
'''
# To get student markst
# check at 40 marks fail or pass

def Marks(marks):
    if(marks >= 40):# 41, 42, 43....39 (false)
        print("You are Pass")
    else:
        print("You are Fail")

    

if __name__=="__main__":
    marks = int(input("Enter your Marks : "))
    Marks(marks)

