'''
Write a Python program to show a message in this format using print function. 
Each character should one tab distance 
A
B	 C
D 	E	 F 
G	 H	 I	 J
K 	L 	M 
N 	O 
P

'''
# display char with tab
'''
print("A")
print("B\tC")
print("D\tE\tF")
print("G\tH\tI\tJ")
print("K\tL\tM")
print("N\tO")
print("P")
'''

def Triangle_ABC(v):
    flag = 1
    for i in range(0,len(v)):
        for j in range(i,i+flag):
            print(v[j],end=" ")
        flag = flag + 1
        print(" ") 
        


if __name__=="__main__":
    #v = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P"]
    v = ["A","B","C","D","E","F","G","H","I","J"]
    Triangle_ABC(v)


