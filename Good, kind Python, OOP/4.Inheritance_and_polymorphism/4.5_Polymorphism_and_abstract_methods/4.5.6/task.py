from abc import ABC, abstractmethod

# здесь объявляйте классы
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    __ID = 0

    def __new__(cls, *args, **kwargs):
        cls.__ID += 1
        return super().__new__(cls)

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self.__id = self.__ID

    def get_pk(self):
        return self.__id
