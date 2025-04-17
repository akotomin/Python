class Descriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if self.name in ('_width', '_height') and value <= 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        instance.__dict__[self.name] = value


class Rect:
    x = Descriptor()
    y = Descriptor()
    width = Descriptor()
    height = Descriptor()

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError('аргумент должен быть объектом класса Rect')
        if (self._x + self._width <= rect._x) or (rect._x + rect._width <= self._x):
            return False
        if (self._y + self._height <= rect._y) or (rect._y + rect._height <= self._y):
            return False
        raise TypeError('прямоугольники пересекаются')


lst_rect = [
    Rect(0, 0, 5, 3),
    Rect(6, 0, 3, 5),
    Rect(3, 2, 4, 4),
    Rect(0, 8, 8, 1)
]

lst_not_collision = []
for i, rect in enumerate(lst_rect):
    collision = False
    for j, other_rect in enumerate(lst_rect):
        if i != j:
            try:
                rect.is_collision(other_rect)
            except TypeError:
                collision = True
                break
    if not collision:
        lst_not_collision.append(rect)
