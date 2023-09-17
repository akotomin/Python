# Подвиг 2. Имеется фрагмент программы (см. листинг ниже). При его выполнении возникает ошибка FileNotFoundError.
# Запишите конструкцию try / except, чтобы отображалось сообщение "File Not Found", если файл не удается открыть.


try:
    f = open("abc.txt")
    try:
        r = f.read(1)
    finally:
        f.close()
except FileNotFoundError:
    print("File Not Found")
