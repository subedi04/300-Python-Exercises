'''
Write a Python Program to Create set that display only even number
'''

if __name__=="__main__":
    st = set()

    for i in range(10):
        st.add(int(input("Enter a set item")))
    # print(st)

    for i in st:
        if i%2 == 0:
            print(i)