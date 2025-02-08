class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        counter = 1
        obj = self.head

        while obj.next is not None:
            obj = obj.next
            counter += 1

        return counter

    def __call__(self, indx, *args, **kwargs):
        return self.linked_lst(indx)

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        if indx == 0 and self.tail == self.head:
            self.head = None
            self.tail = None
            return

        elif indx == 0:
            self.head = self.head.next
            return

        counter = 0
        obj = self.head

        while counter != indx:
            obj = obj.next
            counter += 1

        if obj.next is not None:
            obj.next.prev = obj.prev
            obj.prev.next = obj.next
        else:
            obj.prev.next = None
            self.tail = obj.prev

    def linked_lst(self, indx):
        counter = 0
        obj = self.head

        while counter != indx:
            obj = obj.next
            counter += 1

        return obj.data


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def data(self):
        return self.__data
