# Подвиг 4. Имеется закодированная строка с помощью азбуки Морзе. Коды разделены между собой пробелом.
# Необходимо ее раскодировать, используя азбуку Морзе из предыдущего занятия.
# Полученное сообщение (строку) вывести на экран.
# ====================
# Sample Input:
# .-- ... . -...- .-- . .-. -. ---
# ====================
# Sample Output:
# все верно

morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',
         'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
         'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
         'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}


morze_strig = input().split()
strig = ""

for i in morze_strig:
    for k, v in morze.items():
        if i == v:
            strig = strig + k
            break
print(strig)