# Простой пример с наследованием: говорят, класс Human наследует класс Monkey или Monkey - суперкласс для Human


class Monkey:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print('My name is', self.name)

    def am_i_monkey(self): # возвращает True, если тип объекта - Monkey
        print('Am I monkey?', type(self) == Monkey) # type(self) - класс экземпляра


class Human(Monkey): # суперкласс указывается в скобках после имени класса
    pass # класс Human наследует методы Monkey в том виде, в котором они описаны в Monkey


monkey = Monkey('Innokentyi', 5) # используется конструктор класса Monkey
monkey.say_name() # используется метод say_name класса Monkey
monkey.am_i_monkey() # True поскольку в данному случае self - экземпляр класса Monkey

human = Human('Fedor', 12)  # используется конструктор класса Monkey
human.say_name() # используется метод say_name класса Monkey
human.am_i_monkey() # False, поскольку в данному случае self - экземпляр класса Human