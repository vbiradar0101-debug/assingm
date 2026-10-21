class Book:
    def __init__(self, n, w, p,  price, ):
        self.name = n
        self.writer = w
        self.page = p
        self.price = price

Book1 = Book("Ramayan", "Valmiki",500, 400)
Book2 = Book("mahabharat","ved vyasa",1000, 800)
Book3 = Book("Agnipath","Harivanshi rai bachchan",120, 150)
Book4 = Book("The Jungle Book", "Rudyard Kipling", 300, 350)
Book5 = Book("Harry Potter", "J. K. Rowling", 350, 500)

print("Book list : ")

Book_list = []

Book_list.append(Book1)
Book_list.append(Book2)
Book_list.append(Book3)
Book_list.append(Book4)
Book_list.append(Book5)

for i in Book_list :
    print("name: ",i.name)
    print("writer: ",i.writer)
    print("page no.: ",i.page)
    print("price: ",i.price)
    print("**********************")

