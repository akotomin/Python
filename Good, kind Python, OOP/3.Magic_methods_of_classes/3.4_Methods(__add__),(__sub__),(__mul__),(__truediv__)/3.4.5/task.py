class ListMath:
    def __init__(self, lst=None):
        self.lst_math = self.__check_list(lst if lst is not None else [])

    def __check_list(self, lst):
        return list(filter(lambda x: type(x) in (int, float), lst))

    @staticmethod
    def __value_check(value):
        if not isinstance(value, (int, float)):
            raise ArithmeticError("Правый операнд должен быть типом int или float")

    def __add__(self, other):
        self.__value_check(other)
        return ListMath([i + other for i in self.lst_math])

    def __iadd__(self, other):
        self.__value_check(other)
        self.lst_math = [i + other for i in self.lst_math]
        return self

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        self.__value_check(other)
        return ListMath([i - other for i in self.lst_math])

    def __isub__(self, other):
        self.__value_check(other)
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __rsub__(self, other):
        return ListMath([other - i for i in self.lst_math])

    def __mul__(self, other):
        self.__value_check(other)
        return ListMath([i * other for i in self.lst_math])

    def __imul__(self, other):
        self.__value_check(other)
        self.lst_math = [i * other for i in self.lst_math]
        return self

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        self.__value_check(other)
        return ListMath([i / other for i in self.lst_math])

    def __itruediv__(self, other):
        self.__value_check(other)
        self.lst_math = [i / other for i in self.lst_math]
        return self

    def __rtruediv__(self, other):
        return ListMath([other / i for i in self.lst_math])
