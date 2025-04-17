class Validator:
    value_type = None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != self.value_type or (self.min_value > value or self.max_value < value):
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    value_type = float


class IntegerValidator(Validator):
    value_type = int


def is_valid(lst, validators):
    new_list = []
    for i in lst:
        try:
            validators[0](i)
            new_list.append(i)
        except ValueError:
            try:
                validators[1](i)
                new_list.append(i)
            except ValueError:
                continue

    return new_list


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
print(lst_out)