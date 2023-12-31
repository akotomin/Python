# Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений,
# используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна возвращать значение
# суммы. (Выводить на экран она ничего не должна).
# Вызовите эту функцию и выведите вычисленное значение суммы на экран.
# ====================
# Sample Input:
# 8 11 -5 4 3
# ====================
# Sample Output:
# 21


lst_in = [int(i) for i in input().split()]


def get_rec_sum(lst):
    head, *tail = lst
    return head + get_rec_sum(tail) if tail else head


print(get_rec_sum(lst_in))