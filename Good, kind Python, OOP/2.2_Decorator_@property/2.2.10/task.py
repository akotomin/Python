class PhoneBook:
    def __init__(self):
        self.phonebook = list()

    def add_phone(self, phone):
        self.phonebook.append(phone)

    def remove_phone(self, indx):
        del self.phonebook[indx]

    def get_phone_list(self):
        return self.phonebook


class PhoneNumber:
    def __init__(self, number, fio):
        self.__number = number
        self.__fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if type(number) == int and len(f'{number}') == 11:
            self.__number = number

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        if isinstance(fio, str):
            self.__fio = fio


