# Подвиг 1. Вводится строка. Необходимо найти все индексы фрагмента "ра" во введенной строке. Вывести в строку через
# пробелы найденные индексы. Если этот фрагмент ни разу не будет найден, то вывести значение -1.
# ====================
# Sample Input:
# Барабанщик бил бой в барабан
# ====================
# Sample Output:
# 2 23


s = input()

if 'ра' not in s:
    print(-1)
else:
    for i in range(len(s)-1):
        if s[i] == 'р' and s[i+1] == 'а':
            print(i, end=' ')