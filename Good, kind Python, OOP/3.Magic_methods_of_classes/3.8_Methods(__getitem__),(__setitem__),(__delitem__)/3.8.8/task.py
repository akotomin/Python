class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

    @staticmethod
    def __check_index(index):
        if not (0 <= index[0] < 3 and 0 <= index[1] < 3):
            raise IndexError('неверный индекс клетки')

    def __setitem__(self, key, value):
        self.__check_index(key)
        row, col = key
        cell = self.pole[row][col]
        if not cell.is_free:
            raise ValueError('клетка уже занята')
        cell.value = value
        cell.is_free = False

    def __getitem__(self, key):
        if isinstance(key[0], slice):
            col = key[1]
            return tuple(self.pole[row][col].value for row in range(3))
        elif isinstance(key[1], slice):
            row = key[0]
            return tuple(self.pole[row][col].value for col in range(3))
        else:
            self.__check_index(key)
            row, col = key
            return self.pole[row][col].value
