# здесь объявляйте класс Triangle
class Triangle:
    def __init__(self, a, b, c):
        self._a = self.__check_value(a)
        self._b = self.__check_value(b)
        self._c = self.__check_value(c)
        self.__triangle_valid(self._a, self._b, self._c)

    @staticmethod
    def __check_value(value):
        if (type(value) != int or type(value) != float) and value <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        return value

    def __triangle_valid(self, a, b, c):
        if a > b + c or b > a + c or c > b + a:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')



input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]  # эту строчку не менять (переменную input_data также не менять)

# здесь формируйте список lst_tr
lst_tr = []

for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except (ValueError, TypeError):
        continue