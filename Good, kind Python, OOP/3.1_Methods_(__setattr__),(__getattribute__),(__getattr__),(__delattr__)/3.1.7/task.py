class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        """
        Добавляет новое приложение на смартфон (в конец списка apps)
        :param app: Приложение, которое нужно добавить
        """

        if app.name not in [_.name for _ in self.apps]:
            self.apps.append(app)

    def remove_app(self, app):
        """
        Удаляет приложение по ссылке на объект app.
        :param app: Ссылка на приложение, которое нужно удалить
        """

        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.__name = "ВКонтакте"

    @property
    def name(self):
        return self.__name


class AppYouTube:
    def __init__(self, memory_max):
        self.__name = "YouTube"
        self.memory_max = memory_max

    @property
    def name(self):
        return self.__name


class AppPhone:
    def __init__(self, phone_list: dict):
        self.__name = "Phone"
        self.phone_list = phone_list

    @property
    def name(self):
        return self.__name


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
