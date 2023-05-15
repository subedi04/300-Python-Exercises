'''
Write A Python Program To Generate 1 To 10 Number With Their Square 
And Cube And Also Display Their Addition (Square + Cube)

Expected result:

Number 	Square	Cube 		Addition
1		 1		 1		         1 
2		 4		 8		        12
3		 9		27		        36
'''
# to generate num 1 to 10
# find their square, cube, and addition of square and cube

print("Number\t\t Square\t\t Cube\t\t Addition")
for i in range(1,11):  
    print(str(i)+"\t\t"+str(i*i)+"\t\t"+str(i*i*i)+"\t\t"+str((i*i)+(i*i*i)))