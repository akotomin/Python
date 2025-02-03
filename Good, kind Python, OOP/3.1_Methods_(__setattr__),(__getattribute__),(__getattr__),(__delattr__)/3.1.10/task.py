import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and self.slot_1 is None and type(filter) == Mechanical:
            self.slot_1 = filter
        elif slot_num == 2 and self.slot_2 is None and type(filter) == Aragon:
            self.slot_2 = filter
        elif slot_num == 3 and self.slot_3 is None and type(filter) == Calcium:
            self.slot_3 = filter

    def remove_filter(self, slot_num):
        if isinstance(slot_num, int):
            if slot_num == 1:
                self.slot_1 = None
            elif slot_num == 2:
                self.slot_2 = None
            elif slot_num == 3:
                self.slot_3 = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        filters = self.get_filters()
        if all(filters) and all(0 <= time.time() - i.date <= self.MAX_DATE_FILTER for i in filters):
            return True
        else:
            return False


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return None
        return object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return None
        return object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return None
        return object.__setattr__(self, key, value)


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
