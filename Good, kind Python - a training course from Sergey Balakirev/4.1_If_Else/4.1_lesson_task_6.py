# Подвиг 6. Вводится слово. Проверить, что в этом слове присутствуют все три буквы: t, h и o (в произвольном порядке).
# Реализовать программу с помощью одного условного оператора. Если проверка проходит, вывести ДА, иначе - НЕТ.
# ====================
# Sample Input:
# Python
# ====================
# Sample Output:
# ДА


a = input()
if 't' in a and 'h' in a and 'o' in a:
     print("ДА")
else:
     print("НЕТ")