class Mammal:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name, end=', ')

    def am_i_mammal(self): # определяет метод, который доступен в Mammal и его наследниках
        return isinstance(self, Mammal) # метод возвращает True, если объект является наследником Mammal


class Dog(Mammal):
    def say_name(self): # полностью замещает say_name
        print('woof! I am', self.name)


class Monkey(Mammal):
    def __init__(self, name='Innokentyi', age=5): # полностью замещает конструктор
        self.name = 'Monkey ' + name
        self.age = age

    def say_name(self): # переопределяем метод для Monkey и его наследников
        Mammal.say_name(self) # вызываем метод say_name суперкласса Mammal, аналогично super().say_name()
        print('my name is', self.name)

    def am_i_monkey(self): # определяет метод, который доступен в Monkey и его наследниках
        return type(self) == Monkey


class Human(Monkey):
    pass


dog = Dog('Good Boy')
dog.say_name() # woof! I am Good Boy

monkey = Monkey()
monkey.say_name() # Innokentyi, my name is Innokentyi

human = Human() # в классе не реализованы методы, поэтому будет вызваться конструктор класса Monkey и метод say_name
human.say_name() # Innokentyi, my name is Innokentyi

print('Am I Mammal?', dog.am_i_mammal()) # True
print('Am I Mammal?', monkey.am_i_mammal()) # True
print('Am I Mammal?', human.am_i_mammal()) # True

# print('Am I Monkey?', dog.am_i_monkey()) # ошибка, такого метода нет в классе Dog и классе Mammal, от которого Dog наследуется
print('Am I Monkey?', monkey.am_i_monkey()) # True
print('Am I Monkey?', human.am_i_monkey()) # False