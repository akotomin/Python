# Большой подвиг 10. Объявите два класса:
# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером N x N клеток.
# С помощью класса Cell предполагается создавать отдельные клетки командой:
# c1 = Cell(around_mines, mine)
# Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие
# мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
# around_mines - число мин вокруг клетки (начальное значение 0);
# mine - наличие/отсутствие мины в текущей клетке (True/False);
# fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).
# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и
# все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.
# В классе GamePole должны быть также реализованы следующие методы:
# init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина
# должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается
# символ #; мина отображается символом *; между клетками при отображении ставить пробел).
# При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной
# инициализации игрового поля.
# В классе GamePole могут быть и другие вспомогательные методы.
# Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.
# P.S. На экран в программе ничего выводить не нужно.
import random


class Cell:
    """для представления клетки игрового поля"""
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    """для управления игровым полем, размером N x N клеток"""
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init()

    def init(self):
        # Добавляем мины на поле
        mines = random.sample(range(self.N * self.N), self.M)
        for mine in mines:
            row = mine // self.N
            col = mine % self.N
            self.pole[row][col].mine = True

        # Обновляем параметр around_mines для соседей
        indexes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for x in range(self.N):
            for y in range(self.N):
                if not self.pole[x][y].mine:
                    self.pole[x][y].around_mines = sum(
                        (self.pole[x+i][y+j].mine for i, j in indexes if 0 <= x+i < self.N and 0 <= y+j < self.N)
                    )

    def show(self):
        for row in self.pole:
            print(*map(lambda cell: "#" if not cell.fl_open else cell.around_mines if not cell.mine else '*', row))


pole_game = GamePole(10, 12)
