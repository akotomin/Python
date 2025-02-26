class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    @staticmethod
    def __check_index(indx):
        if not isinstance(indx, int) or indx < 0 or indx > 4:
            raise IndexError('неверный индекс')

    @staticmethod
    def _get_attr_name(indx):
        attributes = ['fio', 'job', 'old', 'salary', 'year_job']
        return attributes[indx]

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self._get_attr_name(item))

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self._get_attr_name(key), value)

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= 5:
            raise StopIteration
        value = getattr(self, self._get_attr_name(self._iter_index))
        self._iter_index += 1
        return value
