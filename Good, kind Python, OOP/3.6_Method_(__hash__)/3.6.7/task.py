import sys


class DataBase:
    def __init__(self, path=None):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        if self.dict_db.get(hash(record)) is None:
            self.dict_db[hash(record)] = [record]
        else:
            self.dict_db[hash(record)].append(record)

    def read(self, pk):
        for records in self.dict_db.values():
            for record in records:
                if record.pk == pk:
                    return record
        return None


class Record:
    PK = 0

    def __new__(cls, *args, **kwargs):
        cls.PK += 1
        return super().__new__(cls)

    def __init__(self, fio, descr, old):
        self.fio = fio if type(fio) == str else None
        self.descr = descr if type(descr) == str else None
        self.old = old if type(old) == int else None
        self.pk = self.PK

    def __hash__(self):
        return abs(hash((self.fio, self.old)))

    def __eq__(self, other):
        if not isinstance(other, Record):
            raise TypeError("Операнд справа должен быть объектом класса Record")

        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase()

for i in lst_in:
    info = i.split(';')
    record = Record(info[0].strip(), info[1].strip(), int(info[2].strip()))
    db.write(record)
