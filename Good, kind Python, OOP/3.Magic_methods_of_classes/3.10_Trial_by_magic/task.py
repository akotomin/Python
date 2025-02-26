from random import choice


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def __getitem__(self, indices):
        i, j = indices
        if not (0 <= i < 3 and 0 <= j < 3):
            raise IndexError('некорректно указанные индексы')
        return self.pole[i][j].value

    def __setitem__(self, indices, value):
        i, j = indices
        if not (0 <= i < 3 and 0 <= j < 3):
            raise IndexError('некорректно указанные индексы')
        if self.pole[i][j].value != self.FREE_CELL:
            raise ValueError('клетка уже занята')
        self.pole[i][j].value = value

    def init(self):
        self.__init__()

    def show(self):
        for row in self.pole:
            print(" | ".join(str(obj.value) for obj in row))
            if row != self.pole[-1]:
                print("-" * 9)

    def human_go(self):
        while True:
            try:
                i, j = map(int, input("Введите координаты (i j): ").split())
                if not (0 <= i < 3 and 0 <= j < 3):
                    print("Координаты должны быть от 0 до 2")
                    continue
                if self.pole[i][j].value != self.FREE_CELL:
                    print("Клетка уже занята")
                    continue
                self[i, j] = self.HUMAN_X
                break
            except ValueError:
                print("Введите два числа через пробел")

    def computer_go(self):
        free_cells = [(i, j) for i in range(3) for j in range(3) if self.pole[i][j].value == self.FREE_CELL]
        if free_cells:
            i, j = choice(free_cells)
            self[i, j] = self.COMPUTER_O

    @property
    def is_human_win(self):
        return self._check_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self._check_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        return not any(
            self.pole[i][j].value == self.FREE_CELL for i in range(3) for j in range(3)
        ) and not self.is_human_win and not self.is_computer_win

    def _check_win(self, player):
        for i in range(3):
            if all(self.pole[i][j].value == player for j in range(3)):
                return True
            if all(self.pole[j][i].value == player for j in range(3)):
                return True
        if all(self.pole[i][i].value == player for i in range(3)):
            return True
        if all(self.pole[i][2 - i].value == player for i in range(3)):
            return True
        return False

    def __bool__(self):
        return not (self.is_human_win or self.is_computer_win or self.is_draw)


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")