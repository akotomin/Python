**Подвиг 7.** В программе объявлена функция `integer_params` для класса `Vector`, которая применяет к каждому методу класса
декоратор `integer_params_decorated`:

```python
def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]
```

Декоратор `integer_params_decorated` должен проверять, чтобы все передаваемые аргументы в методы класса 
(кроме первого `self`) были целыми числами (имели тип `int`).
Если это не так, то должно генерироваться исключение командой:

`raise TypeError("аргументы должны быть целыми числами")` \
Ваша задача объявить эту функцию-декоратор.

Пример использования класса (эти строчки в программе не писать):

```python
vector = Vector(1, 2)
print(vector[1])
vector[1] = 20.4 # TypeError
```

P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.