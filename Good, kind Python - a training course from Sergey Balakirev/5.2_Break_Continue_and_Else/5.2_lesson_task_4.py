# Подвиг 4. Вводится список названий городов в одну строчку через пробел. Определить, что в этом списке все города имеют
# длину более 5 символов. Реализовать программу с использованием цикла while и оператора break. Вывести ДА, если условие
# выполняется и НЕТ - в противном случае.
# ====================
# Sample Input:
# Самара Ульяновск Новгород Воронеж
# ====================
# Sample Output:
# ДА


lst = list(input().split())
index = 0
answer = "ДА"

while index < len(lst):
    if len(lst[index]) > 5:
        index += 1
    else:
        answer = "НЕТ"
        break

print(answer)