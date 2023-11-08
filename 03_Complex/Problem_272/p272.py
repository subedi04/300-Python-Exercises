file = open("listfile.txt","w")

lst = []
for i in range(10):
    lst.append(int(input("Enter a number : ")))


sum = 0
for i in lst:
    sum += i

product = 1
for i in lst:
    product *= i

m = max(lst)
mi = min(lst)

last_e = lst[-1]
first_e = lst[0]

file.write("List items are = "+str(lst)+" \n")
file.write("List Max = "+str(m)+" \n")
file.write("List Min = "+str(mi)+" \n")
file.write("List sum = "+str(sum)+" \n")
file.write("List Product = "+str(product)+" \n")
file.close()
