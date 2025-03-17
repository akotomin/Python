class PointTrack:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *args):
        self.__points = []
        if len(args) == 2 and all(isinstance(arg, (int, float)) for arg in args):
            # Если переданы start_x и start_y
            self.__points.append(PointTrack(args[0], args[1]))
        else:
            # Если переданы объекты PointTrack
            for arg in args:
                if not isinstance(arg, PointTrack):
                    raise TypeError('Аргументы должны быть объектами PointTrack')
                self.__points.append(arg)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        if not isinstance(pt, PointTrack):
            raise TypeError('Аргумент должен быть объектом PointTrack')
        self.__points.append(pt)

    def add_front(self, pt):
        if not isinstance(pt, PointTrack):
            raise TypeError('Аргумент должен быть объектом PointTrack')
        self.__points.insert(0, pt)

    def pop_back(self):
        if not self.__points:
            raise IndexError('Маршрут пуст')
        return self.__points.pop()

    def pop_front(self):
        if not self.__points:
            raise IndexError('Маршрут пуст')
        return self.__points.pop(0)