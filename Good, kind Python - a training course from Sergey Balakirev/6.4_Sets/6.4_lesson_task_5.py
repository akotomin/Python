# Подвиг 5. Вводится строка, содержащая латинские символы, пробелы и цифры. Необходимо выделить из нее все
# неповторяющиеся цифры (символы от 0 до 9) и вывести на экран в одну строку через пробел их в порядке возрастания
# значений. Если цифры отсутствуют, то вывести слово НЕТ.
# ====================
# Sample Input:
# Python 3.9.11 - best language!
# ====================
# Sample Output:
# 1 3 9


string = input()
s = set(string)
lst = []
for i in s:
    try:
        lst.append(int(i))
    except ValueError:
        continue

print(*sorted(lst)) if len(lst) >= 1 else print('НЕТ')