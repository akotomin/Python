# Подвиг 2. На вход программы подается целое десятичное число. Используя битовые операции, включите третий бит
# введенного числа. Выведите на экран полученное числовое значение.


N = int(input())
mask = 0b1000
N = N | mask
print(N)