class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        if not isinstance(other, Book):
            raise ArithmeticError("Правый операнд должен быть типом объектом класса Book")

        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Book):
            if other in self.book_list:
                self.book_list.remove(other)
            else:
                raise ValueError(f"Книги {other} нет в этой библиотеке")
        elif isinstance(other, int):
            self.book_list.pop(other)
        else:
            raise ArithmeticError("Правый операнд должен быть типом объектом класса Book или int")

        return self

    def __isub__(self, other):
        return self - other


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
