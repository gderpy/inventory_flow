
# Механизм инкапсуляции - ограничение доступа к данным и методам класса извне

# attribute - публичное свойство (public)
# _attribute - служит для обращения внутри класса и во всех его дочерних классах (protected)
# __attribute - служит для обращения только внутри класса (private)


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x 
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    # сеттер
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x 
            self.__y = y 
        else:
            raise ValueError("Координаты должны быть числами")

    # геттер
    def get_coord(self):
        return self.__x, self.__y
    
# Класс в ООП следует воспринимать, как единое целое, и чтобы случайно или намеренно
# не нарушить целостность работы алгоритма внутри этого класса, то следует взаимодействовать
# с ним только через публичные свойства и методы. В этом суть принципа инкапсуляции


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt._Point__x)
