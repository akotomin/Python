from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if not isinstance(obj, StackObj):
            raise TypeError("Object must be an instance of StackObj")

        if self._top is None:
            self._top = obj
        else:
            current = self._top
            while current.next is not None:
                current = current.next
            current.next = obj

    def pop_back(self):
        if self._top is None:
            return None

        if self._top.next is None:
            removed_obj = self._top
            self._top = None
            return removed_obj

        current = self._top
        while current.next.next is not None:
            current = current.next

        removed_obj = current.next
        current.next = None
        return removed_obj