# Простейший класс, скрытые методы и атрибуты класса
# __имя_атрибута, __имя_метода - создание скрытого атрибута и метода (2 подчеркивания должно быть только до названия и не должно быть после)

class Student:
    def __init__(self, age, name):
        self.__name = name # "скрытое" поле, недоступно напрямую по имени за пределами класса
        self.age = age

    def __secret_method(self): # "скрытый" метод, недоступен напрямую по имени за пределами класса
        return 'it is the secret method'

    def get_name(self):
        return self.__name


new_student = Student(18, 'Ivan')
# print(new_student.__secret_method()) # вызовет ошибку, метод __secret_method напрямую по имени доступен только внутри класса
# print(new_student.__name) # вызовет ошибку, атрибут __name напрямую по имени доступен только внутри класса
print(new_student.get_name()) # Ivan