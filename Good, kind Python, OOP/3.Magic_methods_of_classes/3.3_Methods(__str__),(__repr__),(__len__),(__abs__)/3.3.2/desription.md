**Подвиг 2.** Объявите класс с именем `Book` (книга), объекты которого создаются командой:

`book = Book(title, author, pages)` \
где: \
`title` - название книги (строка); \
`author` - автор книги (строка); \
`pages` - число страниц в книге (целое число).

Также при выводе информации об объекте на экран командой:

`print(book)` \
должна отображаться строчка в формате:

`"Книга: {title}; {author}; {pages}"`

Например:

`"Книга: Муму; Тургенев; 123"`

Прочитайте из входного потока строки с информацией по книге командой:

`lst_in = list(map(str.strip, sys.stdin.readlines()))` \
(строки идут в порядке: `title`, `author`, `pages`).
Создайте объект класса `Book` и выведите его строковое представление в консоль.

Sample Input:
```python
Python ООП
Балакирев С.М.
1024
```

Sample Output:

```python
Книга: Python ООП; Балакирев С.М.; 1024
```
