import sys


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        if not isinstance(other, BookStudy):
            return False
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = []

for i in lst_in:
    parts = i.split(';')
    name = parts[0].strip()
    author = parts[1].strip()
    year = int(parts[2].strip())
    bs = BookStudy(name, author, year)
    lst_bs.append(bs)

unique_books = len(set(hash(bs) for bs in lst_bs))