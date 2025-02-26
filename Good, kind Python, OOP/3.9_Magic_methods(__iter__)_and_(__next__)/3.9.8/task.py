class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def __iter__(self):
        self._current = self.top
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        obj = self._current
        self._current = self._current.next
        return obj

    def __len__(self):
        counter = 0
        current = self.top
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.next = obj

    def push_front(self, obj):
        obj.next = self.top
        self.top = obj

    def __check_index(self, indx):
        if not isinstance(indx, int) or not 0 <= indx < len(self):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        current = self.top
        for _ in range(item):
            current = current.next
        return current.data

    def __setitem__(self, key, value):
        self.__check_index(key)
        current = self.top
        for _ in range(key):
            current = current.next
        current.data = value
