class Digit:
    def __init__(self, value):
        self.__check_value(value)
        self.value = value

    @staticmethod
    def __check_value(value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, value):
        self.__check_value(value)
        super().__init__(value)

    @staticmethod
    def __check_value(value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        self.__check_value(value)
        super().__init__(value)

    @staticmethod
    def __check_value(value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        self.__check_value(value)
        super().__init__(value)

    @staticmethod
    def __check_value(value):
        if value <= 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        self.__check_value(value)
        super().__init__(value)

    @staticmethod
    def __check_value(value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [
    PrimeNumber(1), PrimeNumber(17), PrimeNumber(89),
    FloatPositive(4.3), FloatPositive(3.1), FloatPositive(0.5),
    FloatPositive(7.2), FloatPositive(9.9)
]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
