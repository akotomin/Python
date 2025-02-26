class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def _check_index(self, row, col):
        if not (isinstance(row, int) and isinstance(col, int)):
            raise IndexError('неверный индекс')
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError('неверный индекс')

    def _check_type(self, value):
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, indices):
        row, col = indices
        self._check_index(row, col)
        return self.cells[row][col].data

    def __setitem__(self, indices, value):
        row, col = indices
        self._check_index(row, col)
        self._check_type(value)
        self.cells[row][col].data = value

    def __iter__(self):
        for row in self.cells:
            yield (cell.data for cell in row)
