class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"{self.title} de {self.author} [Année: ({self.year})]"


class Library:
    def __init__(self):
        self.books = {}
        self.borrow_books = {}

    # Ajouter les méthodes ici

    def add_book(self, book):
        self.books[book.title] = book

    def remove_book(self, book_title):
        if book_title in self.books:
            del self.books[book_title]

    def borrow_book(self, book_title):
        if book_title in self.books:
            book = self.books.pop(book_title)
            self.borrow_books[book_title] = book

    def return_book(self, book_title):
        if book_title in self.borrow_books:
            book = self.borrow_books.pop(book_title)
            self.books[book_title] = book

    def available_books(self):
        for book in self.books.values():
            print(book)

    def borrowed_books_list(self):
        for book in self.borrow_books.values():
            print(book)


book1 = Book("1984", "George", 1960)
book2 = Book("Harry Potter", "Jk", 1999)

library = Library()
library.add_book(book1)
library.add_book(book2)

library.available_books()
library.borrow_book("1984")
print("Livres restant")
library.available_books()
print("Empruntées:")
library.borrowed_books_list()
library.return_book("1984")
print("Livres restant")
library.available_books()

# TODO dict
