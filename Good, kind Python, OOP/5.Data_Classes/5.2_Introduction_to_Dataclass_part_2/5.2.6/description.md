**Подвиг 6.** С помощью декоратора `dataclass`, функции `field` и класса `InitVar`:

`from dataclasses import dataclass, field, InitVar`

объявите `Data Class` с именем `FontData` и следующим набором полей (порядок важен):

```python
name (str: название шрифта);
size (float: размер шрифта);
color (int: цвет шрифта с исключением из операций сравнения и начальным значением 0);
type_font (str: тип шрифта с начальным значением None);
monotype: (InitVar[bool]: с исключением из операций сравнения и начальным значением False)
```

В методе `__post_init__` определите значение атрибута `type_font` со значением `"regular"`, если параметр `monotype` 
равен `False`. В противном случае атрибут `type_font` не менять.

Создайте объект с именем `font` класса `FontData` с данными:

`font: name="Tahoma"; size=22.`

P.S. На экран ничего выводить не нужно.

