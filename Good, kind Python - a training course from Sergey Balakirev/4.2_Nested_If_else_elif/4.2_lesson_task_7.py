# Подвиг 7. Вводится целое число k (1 <= k <= 365). Определить, каким днем недели (понедельник, вторник, среда, четверг,
# пятница, суббота или воскресенье) является k-й день не високосного года, в котором 1 января является понедельником.
# ====================
# Sample Input:
# 121
# ====================
# Sample Output:
# вторник


k = int(input())
a = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
if 1 <= k <= 365:
    if k % 7 == 1:
        print(a[0])
    elif k % 7 == 2:
        print(a[1])
    elif k % 7 == 3:
        print(a[2])
    elif k % 7 == 4:
        print(a[3])
    elif k % 7 == 5:
        print(a[4])
    elif k % 7 == 6:
        print(a[5])
    elif k % 7 == 7:
        print(a[6])