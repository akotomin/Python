class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def data(self):
        return self.__data


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            objs = self.top
            while objs.next is not None:
                objs = objs.next

            objs.next = obj

    def pop_back(self):
        objs = self.top
        prev = None
        while objs.next is not None:
            prev = objs
            objs = objs.next

        prev.next = None

    @staticmethod
    def __value_check(value):
        if not isinstance(value, (StackObj, list)):
            raise ArithmeticError("Правый операнд должен быть объектом StackObj или list")

    def __add__(self, other):
        self.__value_check(other)
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.__value_check(other)
        self.push_back(other)
        return self

    def __mul__(self, other):
        self.__value_check(other)
        for i in other:
            obj = StackObj(i)
            self.push_back(obj)
        return self

    def __imul__(self, other):
        self.__value_check(other)
        for i in other:
            obj = StackObj(i)
            self.push_back(obj)
        return self



obj = StackObj("Some info")
obj1 = StackObj("Some info 2")
obj2 = StackObj("Some info 3")
st = Stack()
st = st + obj
print(st.top.data)
st += obj1
st += obj2
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
print(st.top.next.next.next.next.next.next.data)