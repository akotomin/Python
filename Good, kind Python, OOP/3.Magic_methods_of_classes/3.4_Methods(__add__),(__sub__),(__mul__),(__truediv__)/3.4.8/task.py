class Budget:
    def __init__(self):
        self.it = []

    def add_item(self, it):
        self.it.append(it)

    def remove_item(self, indx):
        self.it.pop(indx)

    def get_items(self):
        return self.it


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money if self.__value_check(money) else None

    @staticmethod
    def __value_check(value):
        return isinstance(value, (int, float))

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ArithmeticError("Правый операнд должен быть объектом Item")
        money = self.money + other.money

        return money

    def __radd__(self, other):
        return self.money + other


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x

print(s)