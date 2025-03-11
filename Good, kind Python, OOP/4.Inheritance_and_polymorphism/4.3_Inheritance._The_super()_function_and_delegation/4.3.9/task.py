class StringDigit(str):
    def __init__(self, string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        super().__init__()

    def __add__(self, other):
        if not isinstance(other, str) or not other.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        if not isinstance(other, str) or not other.isdigit():
            raise ValueError("в строке должны быть только цифры")
        return StringDigit(other + super().__str__())