# Подвиг 11 (на повторение). Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:
# add_message(msg) - добавление нового сообщения в список сообщений;
# remove_message(msg) - удаление сообщения из списка;
# set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет то
# он ставится, если уже есть, то убирается);
# show_last_message(число) - отображение последних сообщений;
# total_messages() - возвращает общее число сообщений.
# Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
# Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения
# со следующим набором локальных свойств:
# text - текст сообщения (строка);
# fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть
# и False - в противном случае, изначально False);
# P.S. Как хранить список сообщений, решите самостоятельно.


class Message:
    """
    Позволяет создавать объекты-сообщения
    :param text: текст сообщения (строка)
    :param fl_like: поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и
    False - в противном случае, изначально False)
    """
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    messages = dict()

    @classmethod
    def add_message(cls, msg):
        """
        Добавляет новое сообщение в список сообщений
        :param msg: сообщение, которое необходимо добавить
        """
        cls.messages[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        """
        Удаляет сообщение из список сообщений
        :param msg: сообщение, которое необходимо удалить
        """
        del cls.messages[id(msg)]

    @classmethod
    def set_like(cls, msg):
        """
        Ставит/убирает лайк для сообщения(если лайка нет то он ставится, если уже есть, то убирается)
        :param msg: сообщение, для которого необходимо поставить/убрать лайк
        """
        if cls.messages[id(msg)].fl_like:
            cls.messages[id(msg)].fl_like = False
        else:
            cls.messages[id(msg)].fl_like = True

    @classmethod
    def show_last_message(cls, number: int):
        """
        Отображает список последних сообщений в заданном колчестве
        :param number: влияет на количество последних сообщений к показу
        """
        return print(list(cls.messages.values())[-number:])

    @classmethod
    def total_messages(cls):
        """
        :return: Возвращает общее число сообщений.
        """
        return len(cls.messages)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
Viber.show_last_message(1)
