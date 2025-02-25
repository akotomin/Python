class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, int):
            raise ValueError('должно быть целое число')
        self.__value = new_value


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.array = [cell() for _ in range(max_length)]

    def __getitem__(self, index):
        self._check_index(index)
        return self.array[index].value

    def __setitem__(self, index, value):
        self._check_index(index)
        self.array[index].value = value

    def _check_index(self, index):
        if not isinstance(index, int) or index < 0 or index >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __str__(self):
        return ' '.join(str(item.value) for item in self.array)