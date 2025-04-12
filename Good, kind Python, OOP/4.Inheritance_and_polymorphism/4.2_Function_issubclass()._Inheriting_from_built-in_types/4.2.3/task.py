class ListInteger(list):
    def __init__(self, lst):
        if all(self.__check_value(value) for value in lst):
            super().__init__(lst)
        else:
            raise TypeError('можно передавать только целочисленные значения')
    
    def __setitem__(self, key, value):
        if self.__check_value(value):
            super().__setitem__(key, value)
        else:
            raise TypeError('можно передавать только целочисленные значения')
    
    def append(self, value):
        if self.__check_value(value):
            super().append(value)

    @staticmethod
    def __check_value(value):
        return isinstance(value, int)
