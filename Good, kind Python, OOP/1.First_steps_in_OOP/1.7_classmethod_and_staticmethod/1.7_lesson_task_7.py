# Подвиг 7. В программе объявлен следующий класс для работы с формами ввода логин/пароль:
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

# Который предполагается использовать следующим образом:
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
# Необходимо прописать классы TextInput и PasswordInput, объекты которых формируются командами:
# login = TextInput(name, size)
# psw = PasswordInput(name, size)
# В каждом объекте этих классов должны быть следующие локальные свойства:
# name - название для поля (сохраняет передаваемое имя, например, "Логин" или "Пароль");
# size - размер поля ввода (целое число, по умолчанию 10).
# Также классы TextInput и PasswordInput должны иметь метод:
# get_html(self) - возвращает сформированную HTML-строку в формате:
# (1-я строка для класса TextInput ; 2-я - для класса PasswordInput)
# <p class='login'><имя поля>: <input type='text' size=<размер поля> />
# <p class='password'><имя поля>: <input type='text' size=<размер поля> />
# Например, для поля login:
# <p class='login'>Логин: <input type='text' size=10 />
# Также классы TextInput и PasswordInput должны иметь метод класса (@classmethod):
# check_name(cls, name) - для проверки корректности переданного имя поля (следует вызывать в инициализаторе)
# по следующим критериям:
# - длина имени не менее 3 символов и не более 50;
# - в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
# Если проверка не проходит, то генерировать исключение командой:
# raise ValueError("некорректное поле name")
# Для проверки допустимых символов в каждом классе должен быть прописан атрибут CHARS_CORRECT:
# CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
# CHARS_CORRECT = CHARS + CHARS.upper() + digits
# По заданию нужно объявить только классы TextInput и PasswordInput с соответствующим функционалом. Более ничего.
# P. S. В данном задании получится дублирование кода в классах TextInput и PasswordInput.
# На данном этапе - это нормально.


from string import ascii_lowercase, digits

# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    length = (3, 50)
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if len(name) < cls.length[0] or len(name) > cls.length[1]:
            raise ValueError("некорректное поле name")
        for letter in name:
            if letter not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return " ".join([f"<p class='login'>{self.name}:", "<input type='text'", f"size={self.size}", "/>"])


class PasswordInput:
    length = (3, 50)
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if len(name) < cls.length[0] or len(name) > cls.length[1]:
            raise ValueError("некорректное поле name")
        for letter in name:
            if letter not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(self.name)

    def get_html(self):
        return " ".join([f"<p class='password'>{self.name}:", "<input type='text'", f"size={self.size}", "/>"])


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
