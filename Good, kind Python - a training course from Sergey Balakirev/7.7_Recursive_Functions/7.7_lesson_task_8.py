# Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел. Необходимо выполнить его сортировку по
# возрастанию с помощью алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.
# Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде
# последовательности чисел, записанных через пробел.
# Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.
# P. S. Теория сортировки в видео предыдущего шага.
# ====================
# Sample Input:
# 8 11 -6 3 0 1 1
# ====================
# Sample Output:
# -6 0 1 1 3 8 11


def merge_two_list(a, b):
    c = []
    i = j = 0
    len_a, len_b = len(a), len(b)
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


s = list(map(int, input().split()))
print(*merge_sort(s))