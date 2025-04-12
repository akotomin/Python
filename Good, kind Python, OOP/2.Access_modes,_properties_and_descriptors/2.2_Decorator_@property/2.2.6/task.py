class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_obj):
        if isinstance(next_obj, StackObj) or next_obj is None:
            self.__next = next_obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next:
                current = current.next
            current.next = obj

    def pop(self):
        if self.top is None:
            return None

        if self.top.next is None:
            popped_obj = self.top
            self.top = None
            return popped_obj

        current = self.top
        while current.next and current.next.next:
            current = current.next

        popped_obj = current.next
        current.next = None
        return popped_obj

    def get_data(self):
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result
