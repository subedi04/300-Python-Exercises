'''
Write A Python Program To Get 5 Author Name 
With Their Book Name And Display First Author
With It's Book Name
'''

def get_data():
    author_books = {}

    for i in range(5):
        author_name = input("Enter author name : ") 
        book_name = input("Enter its book name : ")
        author_books[author_name] = book_name
    return author_books

if __name__=="__main__" :
    author_books = get_data()

    print("First auther is "+str(list(author_books.keys())[0]))
    print("First book is "+str(list(author_books.values())[0]))
#print(author_books)