# Подвиг 4. На вход программы подается целое десятичное число. Используя битовые операции, переключите 3-й и 0-й биты
# введенного числа. Выведите на экран полученное числовое значение.


N = int(input())
mask = 0b01001
N ^= mask
print(N)