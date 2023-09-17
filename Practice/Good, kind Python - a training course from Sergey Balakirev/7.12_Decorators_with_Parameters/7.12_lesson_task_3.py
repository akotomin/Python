# Подвиг 3. Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий
# словарь для замены русских букв на соответствующее латинское написание:
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в нижний
# регистр - малые буквы).
# Определите декоратор с параметром chars и начальным значением " !?", который данные символы преобразует в символ "-"
# и, кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису. Полученный результат
# должен возвращаться в виде строки.
# Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# ====================
# Sample Input:
# Декораторы - это круто!
# ====================
# Sample Output:
# dekoratory-eto-kruto-


def set_params(chars=" !?"):
    def decorator(func):
        def wrapper(*args):
            string = func(*args)
            for c in chars:
                string = string.replace(c, '-')
            while '--' in string:
                string = string.replace('--', '-')
            return string
        return wrapper
    return decorator


@set_params(chars="?!:;,. ")
def switcher(string):
    string = string.lower()
    new_string = ''
    for l in string:
        if l in t:
            new_string += t[l]
        else:
            new_string += l

    return new_string


s = input()
new_string = switcher(s)
print(new_string)