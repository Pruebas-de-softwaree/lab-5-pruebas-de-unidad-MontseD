class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            raise ValueError("The book is already borrowed")
        else:
            print("The borrow is not borrowed")
        self.borrowed = True

    def return_book(self):
        if not self.borrowed:
            raise ValueError("The book is not currently borrowed")
        else:
            self.borrowed = False
            print("The book has been returned successfully")



#if __name__ == "__main__":
    #Book_t= Book('Biografía de Vanessa', 'Ivan', 2024, 'ISBN9001')
    #Book_t.borrow()

if __name__ == "__main__":
    Book_t = Book('La biblioteca de la media noche', 'Matt Haig', 2021, '978-6075507712')
    Book_t.borrowed = True 
    Book_t.return_book()  
