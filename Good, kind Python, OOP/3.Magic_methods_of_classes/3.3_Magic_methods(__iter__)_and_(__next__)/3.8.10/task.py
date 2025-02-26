class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.cells = {}

    def _update_dimensions(self):
        if not self.cells:
            self.rows = 0
            self.cols = 0
        else:
            self.rows = max(row for row, col in self.cells.keys()) + 1
            self.cols = max(col for row, col in self.cells.keys()) + 1

    def add_data(self, row, col, data):
        self.cells[(row, col)] = data
        self._update_dimensions()

    def remove_data(self, row, col):
        if (row, col) not in self.cells:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.cells[(row, col)]
        self._update_dimensions()

    def __getitem__(self, indices):
        row, col = indices
        if (row, col) not in self.cells:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.cells[(row, col)].value

    def __setitem__(self, indices, value):
        row, col = indices
        if (row, col) in self.cells:
            self.cells[(row, col)].value = value
        else:
            self.cells[(row, col)] = Cell(value)
            self._update_dimensions()