# Подвиг 5. Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Необходимо на их основе создать словарь, затем проверить, существуют ли в нем ключи со значениями:
# 'house', 'True' и '5' (все ключи - строки). Если все они существуют, то вывести на экран ДА, иначе - НЕТ.
# ====================
# Sample Input:
# вологда=город house=дом True=1 5=отлично 9=божественно
# ====================
# Sample Output:
# ДА


lst = input().split()
d = dict(i.split('=') for i in lst)
if 'house' and 'True' and '5' in d:
    print('ДА')
else:
    print('НЕТ')