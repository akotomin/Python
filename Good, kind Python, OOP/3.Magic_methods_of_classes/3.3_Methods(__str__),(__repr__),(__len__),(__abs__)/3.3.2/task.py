import sys

class Book:
    def __init__(self, title, author, pages):
        self.title = str(title)
        self.author = str(author)
        self.pages = int(pages)

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


lst_in = list(map(str.strip, sys.stdin.readlines()))

book = Book(*lst_in)
print(book)
