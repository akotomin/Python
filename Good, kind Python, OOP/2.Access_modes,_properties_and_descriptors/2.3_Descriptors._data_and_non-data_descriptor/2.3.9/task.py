class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.max_weight >= self.get_total_weight() + thing.weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        del self.__things[indx]

    def get_total_weight(self):
        return sum(i.weight for i in self.__things)


class Thing:
    def __init__(self, name, weight):
        if self.name_check(name) and self.weight_check(weight):
            self.name = name
            self.weight = weight

    @staticmethod
    def name_check(name):
        return isinstance(name, str)

    @staticmethod
    def weight_check(weight):
        return isinstance(weight, int) or isinstance(weight, float)
