# Подвиг 3. Вводится строка. Нужно создать итератор для перебора символов этой строки. Затем, перебрать через созданный
# итератор все символы до первого пробела. В процессе перебора символы выводить на экран в одну строчку друг за другом
# (без пробелов). Гарантируется, что во введенной строке имеется хотя бы один пробел.
# ====================
# Sample Input:
# Возможно-это будет полезно
# ====================
# Sample Output:
# Возможно-это


a = input()
s = ""
for i in a:
    if i == " ":
        break
    else:
        s += i
print(s)