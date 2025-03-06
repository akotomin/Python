class IteratorAttrs:
    def __iter__(self):
        return iter(self.__dict__.items())


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

