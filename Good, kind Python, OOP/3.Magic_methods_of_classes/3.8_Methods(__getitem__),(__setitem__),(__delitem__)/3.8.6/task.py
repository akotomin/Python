class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.next = obj

    def pop(self):
        if self.top is None:
            return None
        elif self.top.next is None:
            obj = self.top
            self.top = None
            return obj
        else:
            current = self.top
            while current.next.next is not None:
                current = current.next
            obj = current.next
            current.next = None
            return obj

    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0:
            raise IndexError('неверный индекс')
        current = self.top
        count = 0
        while current is not None:
            if count == index:
                return current
            current = current.next
            count += 1
        raise IndexError('неверный индекс')

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index < 0:
            raise IndexError('неверный индекс')
        if index == 0:
            value.next = self.top.next
            self.top = value
        else:
            current = self.top
            count = 0
            while current is not None:
                if count == index - 1:
                    value.next = current.next.next
                    current.next = value
                    return
                current = current.next
                count += 1
            raise IndexError('неверный индекс')