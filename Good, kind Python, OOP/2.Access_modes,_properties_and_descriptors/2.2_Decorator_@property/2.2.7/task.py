class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        # Сеттер в инициализаторе
        self.x = x
        self.y = y

    @classmethod
    def __check_coords(cls, coord):
        return type(coord) in (int, float) and cls.MIN_COORD <= coord <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check_coords(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check_coords(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y


v1 = RadiusVector2D() # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1) # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2) # радиус-вектор с координатами (1; 2)

v1.x = 1024
v1.y = 124125
print(v1.__dict__)
