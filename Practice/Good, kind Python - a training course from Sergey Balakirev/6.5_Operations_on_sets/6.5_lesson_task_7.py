# Подвиг 7. Вводится натуральное число, которое может содержать только простые множители 1, 2, 3, 5 и 7
# (любые из них, не обязательно все). Необходимо разложить введенное число на простые множители и проверить, содержит
# ли оно множители 2, 3 и 5 (обязательно все их, хотя бы один раз). Если это так, то вывести ДА, иначе - НЕТ.
# ====================
# Sample Input:
# 210
# ====================
# Sample Output:
# ДА


s = set()
n = int(input())
st = {2, 3, 5}

for i in range(1, 10):
    if n % i == 0:
        s.add(i)

print('ДА' if st <= s else 'НЕТ')