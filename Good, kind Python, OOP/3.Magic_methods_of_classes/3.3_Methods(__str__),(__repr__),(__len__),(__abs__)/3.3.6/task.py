from math import sqrt

class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    def __abs__(self):
        return sqrt(self.real*self.real + self.img*self.img)

    @staticmethod
    def __check_instance__(value):
        return type(value) in (int, float)

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        if self.__check_instance__(real):
            self.__real = real
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        if self.__check_instance__(img):
            self.__img = img
        else:
            raise ValueError("Неверный тип данных.")


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(cmp.real, cmp.img, c_abs)
