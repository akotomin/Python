class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, indices):
        row, col = indices
        self._check_indices(row, col)
        return self.cells[row][col].value

    def __setitem__(self, indices, value):
        row, col = indices
        self._check_indices(row, col)
        self.cells[row][col].value = value

    def _check_indices(self, row, col):
        if not (0 <= row < self.rows) or not (0 <= col < self.cols):
            raise IndexError('неверные индексы')
