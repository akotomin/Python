class Note:
    __notes = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'

    def __init__(self, name, ton):
        self._name, self._ton = name, ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in self.__notes:
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __notes = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Notes.__instance = None

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note('ре', 0)
        self._mi = Note('ми', 0)
        self._fa = Note('фа', 0)
        self._solt = Note('соль', 0)
        self._la = Note('ля', 0)
        self._si = Note('си', 0)

    def __getitem__(self, item):
        if not (0 <= item < 7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])


notes = Notes()
notes[5]._ton = 2
print(notes[5]._ton)  # ссылка на ноту ми