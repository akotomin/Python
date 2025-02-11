class NewList:
    def __init__(self, lst=None):
        self.list = lst.copy() if lst is not None else []

    def get_list(self):
        return self.list.copy()

    def __sub__(self, other):
        other_list = other.get_list() if isinstance(other, NewList) else other.copy()
        new_list = self.get_list()
        for item in other_list:
            for i in range(len(new_list)):
                if new_list[i] == item and type(new_list[i]) is type(item):
                    del new_list[i]
                    break
        return NewList(new_list)

    def __isub__(self, other):
        other_list = other.get_list() if isinstance(other, NewList) else other.copy()
        temp_list = self.get_list()
        for item in other_list:
            for i in range(len(temp_list)):
                if temp_list[i] == item and type(temp_list[i]) is type(item):
                    del temp_list[i]
                    break
        self.list = temp_list
        return self

    def __rsub__(self, other):
        return NewList(other) - self


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.list)


