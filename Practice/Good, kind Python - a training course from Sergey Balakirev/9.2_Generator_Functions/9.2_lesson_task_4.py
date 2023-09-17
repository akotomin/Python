# Подвиг 4. Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:
from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase
# задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной
# в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru
# Для формирования случайного индекса для строки chars используйте функцию randint модуля random:
import random
random.seed(1)
# indx = random.randint(0, len(chars)-1)
# Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно.
# Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
# ==================
# Sample Input:
# 8
# ==================
# Sample Output:
# iKZWeqhF@mail.ru
# WCEPyYng@mail.ru
# FbyBMWXa@mail.ru
# SCrUZoLg@mail.ru
# ubbbPIay@mail.ru


N = int(input())


def pass_generator(n: int, symbols: str, qty=5,) -> str:
    for i in range(qty):
        password = ""
        while len(password) < n:
            password = password + symbols[random.randint(0, len(symbols))]

        yield password + "@mail.ru"


a = pass_generator(N, chars)

for i in range(5):
    print(next(a))