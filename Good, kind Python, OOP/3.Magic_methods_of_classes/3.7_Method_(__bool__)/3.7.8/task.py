import random


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int) or value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open

class GamePole:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        mines = random.sample(range(self.N * self.M), self.total_mines)
        for mine in mines:
            row = mine // self.M
            col = mine % self.M
            self.__pole_cells[row][col].is_mine = True

        for i in range(self.N):
            for j in range(self.M):
                if not self.__pole_cells[i][j].is_mine:
                    count = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < self.N and 0 <= nj < self.M and self.__pole_cells[ni][nj].is_mine:
                                count += 1
                    self.__pole_cells[i][j].number = count

    def open_cell(self, i, j):
        if not (0 <= i < self.N and 0 <= j < self.M):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        for row in self.__pole_cells:
            for cell in row:
                if cell.is_open:
                    if cell.is_mine:
                        print('*', end=' ')
                    else:
                        print(cell.number, end=' ')
                else:
                    print('#', end=' ')
            print()