**Подвиг 3.** С помощью декоратора `dataclass` и функции `field`:

`from dataclasses import dataclass, field`

объявите `Data Class` с именем `PolyLine` и следующим набором полей (порядок важен):


`width (float: с исключением из операций сравнения)`; \
`color (int: с исключением из операций сравнения и начальным значением 0);` \
`points (list: список с начальным значением кортежа (0, 0), то есть, первый элемент списка - это кортеж (0, 0))`.

Создайте два объекта с именами pl1, pl2 класса PolyLine с данными:

```python
pl1: width=0.5; color=0;
pl2: width=1.5; color=2.
```

После этого добавьте в объекты следующие координаты (в список points):

```python
pl1: [(10, -5), (12, 1)];
pl2: [(10, -5), (12, 1)].
```

Выполните сравнение на равенство этих двух объектов. Результат (булево значение) сохраните в переменной res.

P.S. На экран ничего выводить не нужно.