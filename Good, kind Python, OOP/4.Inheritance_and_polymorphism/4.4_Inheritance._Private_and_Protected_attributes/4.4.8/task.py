class Aircraft:
    def __init__(self, model, mass, speed, top):
        if type(model) != str:
            raise TypeError('неверный тип аргумента')
        self._model = model
        self._mass = self.__value_check(mass)
        self._speed = self.__value_check(speed)
        self._top = self.__value_check(top)

    @staticmethod
    def __value_check(value):
        if value <= 0:
            raise TypeError('неверный тип аргумента')
        return value


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self.__value_check(chairs)

    @staticmethod
    def __value_check(value):
        if value > 0 and type(value) == int:
            return value
        raise TypeError('неверный тип аргумента')


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = self.__value_check(weapons)

    @staticmethod
    def __value_check(value):
        if type(value) != dict:
            raise TypeError('неверный тип аргумента')
        return value


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]