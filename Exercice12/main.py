class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    # Ajouter les méthodes ici

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                return

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                return

    def available_books(self):
        for book in self.books:
            print(book.title)

    def borrowed_books_list(self):
        for book in self.borrow_books:
            print(book.title)


book1 = Book("1984", "George", 1960)
book2 = Book("Harry Potter", "Jk", 1999)

library = Library()
library.add_book(book1)
library.add_book(book2)

print(library.available_books())
library.borrow_book("1984")
print("Livres restant", library.available_books())
print("Empruntées:", library.borrowed_books_list())
library.return_book("1984")
print("Livres restant", library.available_books())

# TODO dict
