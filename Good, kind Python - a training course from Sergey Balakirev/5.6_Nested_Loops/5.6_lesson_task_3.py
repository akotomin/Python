# Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть, в
# диапазоне [2; n). Результат вывести на экран в строчку через пробел.
# ====================
# Sample Input:
# 11
# ====================
# Sample Output:
# 2 3 5 7


n = int(input())
lst = [i for i in range(n)]
lst[1] = 0
p = 2
index = 0
newlist = []

while p < n:
    if lst[p] != 0:
        j = p * 2
        while j < n:
            lst[j] = 0
            j = j + p
        p += 1
    else:
        while index < len(lst):
            if lst[index] != 0:
                newlist.append(lst[index])
            index += 1
        else:
            p += 1

print(*newlist)