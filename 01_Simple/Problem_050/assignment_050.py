'''
Write A Python Program To Find Area Of Triangle And 
Then Get A Number From The User, 
Find Square Of That Number. 
Then Add With Area Of The Triangle. 
Total Result Display To User
'''

def Area_Triangle(b,h):
    return (b*h)/2

def square_num(n):
    return n*n

if __name__=="__main__":
    b = float(input("Enter Base   : "))
    h = float(input("Enter Height : "))
    area_t = Area_Triangle(b,h)

    n = float(input("Enter a number : "))
    sq = square_num(n)

    print("Area of the triangle is = "+str(area_t))
    print("Square of number is : " + str(sq))
    print("The total is : ", str(area_t + sq))