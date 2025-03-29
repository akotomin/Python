# здесь объявляйте класс
class TupleLimit(tuple):
    def __new__(cls, lst, length):
        instance = super().__new__(cls, lst)
        instance.length = length
        return instance

    def __init__(self, lst, max_lenght):
        if len(lst) > max_lenght:
            raise ValueError('число элементов коллекции превышает заданный предел')
        self.lst = lst
        self.max_lenght = max_lenght

    def __str__(self):
        return ' '.join(str(i) for i in self.lst)

    def __repr__(self):
        return ' '.join(str(i) for i in self.lst)



digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

# здесь создавайте объект класса
try:
    tl = TupleLimit(digits, 5)
    print(tl)
except ValueError as ve:
    print(ve)