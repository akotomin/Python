# Подвиг 12. Составить программу поиска всех трехзначных чисел, которые при делении на 47 дают в остатке 43 и кратны 3.
# Вывести найденные числа в строчку через пробел. Программу реализовать при помощи цикла while.
# ====================
# Sample Input:
# ====================
# Sample Output:
# 231 372 513 654 795 936


start, stop = 100, 999

while start <= stop:
    if start % 47 == 43 and start % 3 == 0:
        print(start, end=" ")
    start += 1