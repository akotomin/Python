# Подвиг 5. Вводится список вещественных чисел и список названий городов, каждый в отдельной строке.
# Необходимо сформировать единый список lst, в котором сначала идут числа, а затем, названия городов.
# Реализовать программу с помощью оператор распаковки *. Вывести полученный список на экран командой:
# print(*lst)
# ====================
# Sample Input:
# 5.8 11.0 4.3
# Уфа Омск Тверь Самара
# ====================
# Sample Output:
# 5.8 11.0 4.3 Уфа Омск Тверь Самара


numbers = list(map(float, input().split()))
cities = input().split()
lst = [*numbers, *cities]
print(*lst)
