# здесь объявляйте классы CellException, CellIntegerException, CellFloatException, CellStringException
class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


# здесь объявляйте классы CellInteger, CellFloat, CellString
class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not (self._min_value <= val <= self._max_value):
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = val


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not (self._min_value <= val <= self._max_value):
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._value = val


class CellString:
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not (self._min_length <= len(val) <= self._max_length):
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._value = val


# здесь объявляйте класс TupleData
class TupleData:
    def __init__(self, *args):
        self.cells = list(args)

    def __len__(self):
        return len(self.cells)

    def __getitem__(self, index):
        if not (0 <= index < len(self.cells)):
            raise IndexError
        return self.cells[index].value

    def __setitem__(self, index, value):
        if not (0 <= index < len(self.cells)):
            raise IndexError
        self.cells[index].value = value

    def __iter__(self):
        for cell in self.cells:
            yield cell.value


# эти строчки в программе не менять!
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")