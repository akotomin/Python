# здесь объявляйте декоратор и все что с ним связано
def class_log(log_list):
    def decorator(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            def make_wrapper(method):
                def wrapper(*args, **kwargs):
                    log_list.append(method.__name__)
                    return method(*args, **kwargs)
                return wrapper
            setattr(cls, k, make_wrapper(v))
        return cls
    return decorator


vector_log = []   # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value