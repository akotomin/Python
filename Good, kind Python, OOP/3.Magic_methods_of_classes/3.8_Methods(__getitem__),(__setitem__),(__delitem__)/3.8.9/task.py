class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []

    def __check_weight(self, new_thing=None):
        total_weight = sum(thing.weight for thing in self.things)
        if new_thing:
            total_weight += new_thing.weight
        if total_weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing):
        self.__check_weight(thing)
        self.things.append(thing)

    def __check_index(self, index):
        if not (0 <= index < len(self.things)):
            raise IndexError('неверный индекс')

    def __getitem__(self, index):
        self.__check_index(index)
        return self.things[index]

    def __setitem__(self, index, thing):
        self.__check_index(index)
        old_thing = self.things[index]
        self.things[index] = thing
        try:
            self.__check_weight()
        except ValueError:
            self.things[index] = old_thing
            raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, index):
        self.__check_index(index)
        del self.things[index]