class Vector:
    def __init__(self, *coords):
        self.coords = list(coords)

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            return Vector(*[a + b for a, b in zip(self.coords, other.coords)])
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            return Vector(*[a - b for a, b in zip(self.coords, other.coords)])
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            return Vector(*[a * b for a, b in zip(self.coords, other.coords)])
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [a + other for a in self.coords]
        elif isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            self.coords = [a + b for a, b in zip(self.coords, other.coords)]
        else:
            return NotImplemented
        return self

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [a - other for a in self.coords]
        elif isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            self.coords = [a - b for a, b in zip(self.coords, other.coords)]
        else:
            return NotImplemented
        return self

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.coords == other.coords
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Vector):
            return self.coords != other.coords
        else:
            return NotImplemented
