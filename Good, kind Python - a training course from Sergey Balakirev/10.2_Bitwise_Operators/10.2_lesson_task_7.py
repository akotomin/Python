# Подвиг 7. Вводится зашифрованное слово. Шифрование кодов символов этого слова было проведено с помощью битовой
# операции XOR с ключом key=123. То есть, каждый символ был преобразован по алгоритму:
# x = ord(x) ^ key
# Здесь ord - функция, возвращающая код символа x. Расшифруйте введенное слово и выведите его на экран.
# P. S. Подсказка: для преобразования кода в символ используйте функцию chr.
# ====================
# Sample Input:
# ѩкю[щюлцхZ
# ====================
# Sample Output:
# Все верно!


word = input()
key = 123


for i in word:
    print(chr(ord(i) ^ key), end='')