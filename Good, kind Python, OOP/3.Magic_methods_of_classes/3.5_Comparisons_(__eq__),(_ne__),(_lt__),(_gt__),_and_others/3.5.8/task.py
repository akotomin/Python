class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class MoneyR:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __check_and_converse(self, volume):
        if not isinstance(volume, (MoneyE, MoneyD, MoneyR)):
            raise TypeError("Операнд справа должен быть объектом типа MoneyE или MoneyD или MoneyR")

        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        rub_rate = self.cb.rates['rub']
        eur_rate = self.cb.rates['euro']

        if type(volume) == MoneyD:
            operand = round(volume.volume * rub_rate, 1)
        elif type(volume) == MoneyE:
            operand = round(volume.volume * rub_rate * eur_rate, 1)
        else:
            operand = round(volume.volume, 1)

        return operand


    def __eq__(self, other):
        operand = self.__check_and_converse(other)
        result = any(
            (
                self.volume == operand,
                self.volume == operand + 0.1,
                self.volume == operand - 0.1
            )
        )

        return result

    def __lt__(self, other):
        operand = self.__check_and_converse(other)
        result = any(
            (
                self.volume < operand,
                self.volume < operand + 0.1,
                self.volume < operand - 0.1
            )
        )

        return result

    def __gt__(self, other):
        operand = self.__check_and_converse(other)
        result = any(
            (
                self.volume > operand,
                self.volume > operand + 0.1,
                self.volume > operand - 0.1
            )
        )

        return result

    def __ge__(self, other):
        operand = self.__check_and_converse(other)
        result = any(
            (
                self.volume >= operand,
                self.volume >= operand + 0.1,
                self.volume >= operand - 0.1
            )
        )

        return result


class MoneyE:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __check_and_converse(self, volume):
        if not isinstance(volume, (MoneyE, MoneyD, MoneyR)):
            raise TypeError("Операнд справа должен быть объектом типа MoneyE или MoneyD или MoneyR")

        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        rub_rate = self.cb.rates['rub']
        eur_rate = self.cb.rates['euro']

        if type(volume) == MoneyD:
            operand = round(volume.volume * rub_rate, 1)
        elif type(volume) == MoneyE:
            operand = round(self.volume * rub_rate * eur_rate, 1)
        else:
            operand = round(volume.volume, 1)

        rub_volume = round(self.volume * rub_rate * eur_rate, 1)

        return operand, rub_volume

    def __eq__(self, other):
        operand, rub_volume = self.__check_and_converse(other)
        result = any(
            (
                rub_volume == operand,
                rub_volume == operand + 0.1,
                rub_volume == operand - 0.1
            )
        )

        return result

    def __lt__(self, other):
        operand, rub_volume = self.__check_and_converse(other)
        result = any(
            (
                rub_volume < operand,
                rub_volume < operand + 0.1,
                rub_volume < operand - 0.1
            )
        )

        return result

    def __gt__(self, other):
        operand, rub_volume = self.__check_and_converse(other)
        result = any(
            (
                rub_volume > operand,
                rub_volume > operand + 0.1,
                rub_volume > operand - 0.1
            )
        )

        return result

    def __ge__(self, other):
        operand, rub_volume = self.__check_and_converse(other)
        result = any(
            (
                rub_volume >= operand,
                rub_volume >= operand + 0.1,
                rub_volume >= operand - 0.1
            )
        )

        return result


class MoneyD:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __check_and_converse(self, volume):
        if not isinstance(volume, (MoneyE, MoneyD, MoneyR)):
            raise TypeError("Операнд справа должен быть объектом типа MoneyE или MoneyD или MoneyR")

        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

        rub_rate = self.cb.rates['rub']
        eur_rate = self.cb.rates['euro']

        if type(volume) == MoneyD:
            operand = round(self.volume * rub_rate, 1)
        elif type(volume) == MoneyE:
            operand = round(volume.volume * rub_rate * eur_rate, 1)
        else:
            operand = round(volume.volume, 1)

        rub_volume = round(self.volume * rub_rate, 1)
        return operand, rub_volume


    def __eq__(self, other):
        operand, rub_volume = self.__check_and_converse(other)
        result = any(
            (
                rub_volume == operand,
                rub_volume == operand + 0.1,
                rub_volume == operand - 0.1
            )
        )

        return result

    def __lt__(self, other):
        operand, rub_volume = self.__check_and_converse(other)
        result = any(
            (
                rub_volume < operand,
                rub_volume < operand + 0.1,
                rub_volume < operand - 0.1
            )
        )

        return result

    def __gt__(self, other):
        operand, rub_volume = self.__check_and_converse(other)
        result = any(
            (
                rub_volume > operand,
                rub_volume > operand + 0.1,
                rub_volume > operand - 0.1
            )
        )

        return result

    def __ge__(self, other):
        operand, rub_volume = self.__check_and_converse(other)
        result = any(
            (
                rub_volume >= operand,
                rub_volume >= operand + 0.1,
                rub_volume >= operand - 0.1
            )
        )

        return result
