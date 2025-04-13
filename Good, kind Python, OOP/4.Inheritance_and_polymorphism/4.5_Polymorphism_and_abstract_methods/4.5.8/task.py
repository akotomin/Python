from abc import ABC, abstractmethod

# здесь объявляйте классы
class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        """Абстрактный объект-свойство, название страны"""

    @property
    @abstractmethod
    def population(self):
        """Абстрактный объект-свойство, численность населения"""

    @property
    @abstractmethod
    def square(self):
        """Абстрактный объект-свойство, площадь страны"""

    @abstractmethod
    def get_info(self):
        """Абстрактный метод для получения сводной информации о стране"""


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = population

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, square):
        self._square = square

    def get_info(self):
        return f"{self._name}: {self._square}, {self._population}"


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000
