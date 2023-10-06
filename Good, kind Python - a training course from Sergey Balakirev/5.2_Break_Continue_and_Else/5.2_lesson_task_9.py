# Подвиг 9. (На использование цикла while). Вводятся названия книг (каждое с новой строки). Удалить из введенного списка
# все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом). Результат вывести на экран в
# виде строки из оставшихся названий через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки
# ====================
# Sample Input:
# Муму
# Евгений Онегин
# Сияние
# Мастер и Маргарита
# Пиковая дама
# Колобок
# ====================
# Sample Output:
# Муму Сияние Колобок


import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

i = 0
while len(lst_in) > i:
    if lst_in[i].count(" ") >= 1:
        del lst_in[i]
    else:
        i += 1

print(*lst_in)