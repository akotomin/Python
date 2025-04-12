class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.keys = list(self.__dict__.keys())

    def __getitem__(self, item):
        if not isinstance(item, int) or item < 0 or item >= len(self.keys):
            raise IndexError('неверный индекс поля')
        key = self.keys[item]
        return self.__dict__[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0 or key >= len(self.keys):
            raise IndexError('неверный индекс поля')
        key_name = self.keys[key]
        self.__dict__[key_name] = value
