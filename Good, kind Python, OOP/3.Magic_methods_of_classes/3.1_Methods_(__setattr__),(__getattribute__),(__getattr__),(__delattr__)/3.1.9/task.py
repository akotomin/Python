class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        # Устанавливаем значения через object.__setattr__, чтобы обойти __setattr__
        object.__setattr__(self, "_Dimensions__a", self._validate_value(a))
        object.__setattr__(self, "_Dimensions__b", self._validate_value(b))
        object.__setattr__(self, "_Dimensions__c", self._validate_value(c))

    def _validate_value(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            return value
        return None

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__a = value  # Изменяем, только если значение в диапазоне

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__c = value

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError
