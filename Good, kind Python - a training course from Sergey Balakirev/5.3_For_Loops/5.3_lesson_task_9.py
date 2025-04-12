# Подвиг 9. Вводится список названий городов в одну строчку через пробел. Перебрать все эти названия с помощью цикла for
# и определить, начинается ли название следующего города на последнюю букву предыдущего города в списке. Если последними
# встречаются буквы 'ь', 'ъ', 'ы', то берется следующая с конца буква. Вывести на экран ДА, если последовательность
# удовлетворяет этому правилу и НЕТ - в противном случае.
# ====================
# Sample Input:
# Москва Астрахань Новгород Димитровград Душанбе
# ====================
# Sample Output:
# ДА


lst = input().split()
firstLtr = 0
secondLtr = - 1
i = 0
lstLen = len(lst)

for x in range(lstLen - 1):
        if str.lower(lst[x][secondLtr]) == "ь" \
                or str.lower(lst[x][secondLtr]) == "ъ" \
                or str.lower(lst[x][secondLtr]) == "ы":
            secondLtr = -2
        if str.lower(lst[x][secondLtr]) == str.lower(lst[(x + 1)][firstLtr]):
            i += 1
        secondLtr = -1
if i == lstLen - 1:
    print("ДА")
else:
    print("НЕТ")