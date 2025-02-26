# Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python),
# когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:
# Для этого объявите класс LinkedList, который будет представлять связный список в целом
# и иметь набор следующих методов:
# add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
# remove_obj(self) - удаление последнего объекта из связного списка;
# get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.
# И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:
# head - ссылка на первый объект связного списка (если список пустой, то head = None);
# tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
# Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
# __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
# __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
# __data - строка с данными.
# Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
# set_next(self, obj) - изменение приватного свойства __next на значение obj;
# set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
# get_next(self) - получение значения приватного свойства __next;
# get_prev(self) - получение значения приватного свойства __prev;
# set_data(self, data) - изменение приватного свойства __data на значение data;
# get_data(self) - получение значения приватного свойства __data.
# Создавать объекты класса ObjList предполагается командой:
# ob = ObjList("данные 1")
# А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
# Объявите в программе классы LinkedList и ObjList в соответствии с заданием.
# P.S. На экран ничего выводить не нужно.


class ObjList:
    __next = None
    __prev = None

    def __init__(self, data):
        self.__data = data

    def set_next(self, obj):
        """
        Изменяет приватное свойство __next на значение obj
        """
        self.__next = obj

    def set_prev(self, obj):
        """
        Изменяет приватное свойство __prev на значение obj
        """
        self.__prev = obj

    def set_data(self, data):
        """
        Изменяет приватное свойство __data на значение data
        """
        self.__data = data

    def get_next(self):
        """
        Получает значение приватного свойства __next
        """
        return self.__next

    def get_prev(self):
        """
        Получает значение приватного свойства __prev
        """
        return self.__prev

    def get_data(self):
        """
        Получает значение приватного свойства __data
        """
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def add_obj(self, obj: ObjList):
        """
        Добавляет новый объект класса ObjList в конец связного списка
        :params obj: объект класса ObjList
        """
        if self.head is None:
            self.head = obj
            self.tail = obj
            self.counter += 1
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
            self.counter += 1

    def remove_obj(self):
        """
        Удаляет последний объект из связного списка
        """
        self.tail = self.tail.get_prev()
        self.counter -= 1

    def get_data(self):
        """
        Получает список из строк локального свойства __data всех объектов связного списка
        """
        lst = []
        obj = None
        for _ in range(self.counter):
            if _ == 0:
                obj = self.head.get_next()
                lst.append(self.head.get_data())
            else:
                if obj is None:
                    break
                lst.append(obj.get_data())
                obj = obj.get_next()

        return lst


lst = LinkedList()
for i in range(34):
    lst.add_obj(ObjList(f"данные {i}"))

for _ in range(34):
    lst.remove_obj()

print(lst.get_data())
