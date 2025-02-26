class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i + 1):
                try:
                    yield self.lst[i][j]
                except IndexError:
                    raise IndexError('index out of range')