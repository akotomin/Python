class Singleton:
    __main_instance = None
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__main_instance is None:
                cls.__main_instance = super().__new__(cls)
                return cls.__main_instance

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name

