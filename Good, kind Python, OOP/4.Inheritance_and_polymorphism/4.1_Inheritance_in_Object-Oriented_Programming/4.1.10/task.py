class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def get_coords(self):
        return self.coords

    def _len_coords(self, coords):
        if len(self.coords) != len(coords):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self._len_coords(other.coords)
        new_coords = tuple(a + b for a, b in zip(self.coords, other.coords))
        return Vector(*new_coords)

    def __sub__(self, other):
        self._len_coords(other.coords)
        new_coords = tuple(a - b for a, b in zip(self.coords, other.coords))
        return Vector(*new_coords)


class VectorInt(Vector):
    def __init__(self, *coords):
        if not all(isinstance(x, int) for x in coords):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*coords)

    def __add__(self, other):
        result = super().__add__(other)
        if any(isinstance(x, float) for x in result.coords):
            return Vector(*result.coords)
        return VectorInt(*result.coords)

    def __sub__(self, other):
        result = super().__sub__(other)
        if any(isinstance(x, float) for x in result.coords):
            return Vector(*result.coords)
        return VectorInt(*result.coords)