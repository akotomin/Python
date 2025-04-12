# Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо
# запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:
# em = EmailValidator() # None
# В самом классе реализовать следующие методы класса (@classmethod):
# get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой
# допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
# check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.
# Корректность строки email определяется по следующим критериям:
# - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
# - длина email до символа @ не должна превышать 100 (сто включительно);
# - длина email после символа @ не должна быть больше 50 (включительно);
# - после символа @ обязательно должна идти хотя бы одна точка;
# - не должно быть двух точек подряд.
# Также в классе нужно реализовать приватный статический метод класса:
# is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.
# Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр
# email не является строкой, то check_email() возвращает False.
# Пример использования класса EmailValidator (эти строчки в программе писать не нужно):
# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False
# P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.


from string import ascii_lowercase, digits
import random


class EmailValidator:
    LETTERS = ascii_lowercase + digits + "_" + "."

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        return ''.join(random.choices(cls.LETTERS, k=random.choice(range(100)))) + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

    @classmethod
    def check_email(cls, email):
        at_counter = 0
        point_status = None

        if not cls.__is_email_str(email):
            return False

        if '@' not in email:
            return False

        for i in email:
            if i == '.':
                if point_status is not None:
                    return False
                point_status = '.'
            elif i == '@' and at_counter == 0:
                point_status = None
            elif i in cls.LETTERS:
                point_status = None
            else:
                return False

        split = email.split('@')
        if len(split[0]) > 100 or len(split[1]) > 50 or '.' not in split[1]:
            return False

        return True
