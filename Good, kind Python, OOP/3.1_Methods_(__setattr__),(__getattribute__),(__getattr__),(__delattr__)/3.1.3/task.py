class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)
                break


class Telecast:
    def __init__(self, id, name, duration):
        self.uid = id
        self.name = name
        self.duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, id):
        if isinstance(id, int) and id > 0:
            self.__id = id
        else:
            raise TypeError("Присваивать можно только натуральные числа.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError("Присваивать можно только строки.")

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if isinstance(duration, int):
            self.__duration = duration
        else:
            raise TypeError("Присваивать можно только целые числа.")


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration},  {t.uid}")
