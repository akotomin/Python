# Подвиг 3. Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль
# длиной N символов из случайных букв, цифр и некоторых других знаков. Для получения последовательности допустимых
# символов для генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг
# ниже), на основе которых формируется общий список:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N
# и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс indx в
# диапазоне [a; b] для символа можно с помощью функции randint модуля random:
# import random
# random.seed(1)
# indx = random.randint(a, b)
# Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).
# ==================
# Sample Input:
# 10
# ==================
# Sample Output:
# riGp?58WAm
# !dX3a5IDnO
# dcdbWB2d*C
# 4?DSDC6Lc1
# mxLpQ@2@yM


import random
from string import ascii_lowercase, ascii_uppercase


random.seed(1)
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
N = int(input())


def pass_generator(n: int, symbols: str, qty=5,) -> str:
    for i in range(qty):
        password = ""
        while len(password) < n:
            password = password + symbols[random.randint(0, len(symbols))]

        yield password


a = pass_generator(N, chars)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))