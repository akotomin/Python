class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

        temp_values = instance.__dict__.copy()
        temp_values[self.name] = value

        if all(attr in temp_values for attr in ('a', 'b', 'c')):
            if (temp_values['a'] >= temp_values['b'] + temp_values['c'] or
                    temp_values['b'] >= temp_values['a'] + temp_values['c'] or
                    temp_values['c'] >= temp_values['a'] + temp_values['b']):
                raise ValueError("с указанными длинами нельзя образовать треугольник")

        instance.__dict__[self.name] = value


class Triangle:
    a = PositiveNumber()
    b = PositiveNumber()
    c = PositiveNumber()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        a, b, c = self.a, self.b, self.c
        p = 0.5 * (a + b + c)
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
