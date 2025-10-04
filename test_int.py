from library import Library
from book import Book
from user import User

#if __name__ == "__main__":
    #Library_t = Library()
    #Library_t.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960, "ISBN002"))
    #Book_t= Book("To Kill a Mockingbird", "Harper Lee", 1960, "ISBN002")
    #Book_t.borrow()

if __name__ == "__main__":
    Library_t = Library()
    Book_t = Book("Pride and Prejudice", "Jane Austen", 1813, "ISBN005")
    Library_t.add_book(Book_t)
    Book_t.borrow()
    Book_t.borrow()
    