# Подвиг 7. Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д.
# Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров
# (следующих в том же порядке, что и во входной строке) с соответствующими кодами. Полученный словарь вывести командой:
# print(*sorted(d.items()))
# ====================
# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
#  ====================
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890'])
# ('+7', ['+71234567890', '+71234567854', '+71232267890'])

lst = input().split()
d = {}
for i in lst:
    c = i[:2]
    if c in d:
        d[c].append(i)
    else:
        d[c] = [i]
print(*sorted(d.items()))