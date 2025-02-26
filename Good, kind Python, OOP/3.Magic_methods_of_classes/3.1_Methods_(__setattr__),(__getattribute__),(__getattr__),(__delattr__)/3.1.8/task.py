class Circle:
    def __init__(self, x, y, radius):
        self.__x = self.__y = self.__radius = None
        self.x = x
        self.y = y
        self.radius = radius

    def __setattr__(self, key, value):
        if key in ('x', 'y', 'radius') and type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'radius' and value < 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius


circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
print(circle.x, circle.y)