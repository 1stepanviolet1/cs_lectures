# поля класса доступны через имя класса и одинаковы для всех экземпляров, которые не переопределили его

class Counter:
    counter = 0

    def __init__(self):
        Counter.counter += 1

    def change_with_self(self):
        self.counter += 1

    def change(self):
        Counter.counter = 0


first = Counter()
second = Counter()
third = Counter()

print(first.counter)  # 3
print(second.counter)  # 3
print(third.counter)  # 3
print(Counter.counter, end='\n\n')  # 3

print('-' * 80, end='\n\n')

first.counter += 1  # поле counter переопределено для экземпляра first, мы не меняем объект, мы присваиваем first.counter новое число
print(first.counter)  # 4
print(second.counter)  # 3
print(third.counter)  # 3
print(Counter.counter, end='\n\n')  # 3

print('-' * 80, end='\n\n')

first.change_with_self()  # поле counter переопределено для экземпляра first, поле меняется только у first
print(first.counter)  # 5
print(second.counter)  # 3
print(third.counter)  # 3
print(Counter.counter, end='\n\n')  # 3

print('-' * 80, end='\n\n')

second.change_with_self()  # поле counter переопределено для экземпляра second, мы не меняем объект, мы присваиваем second.counter новое число
print(first.counter)  # 5
print(second.counter)  # 4
print(third.counter)  # 3
print(Counter.counter, end='\n\n')  # 3

print('-' * 80, end='\n\n')

first.change()  # меняем поле класса, не экземпляра
print(first.counter)  # 5
print(second.counter)  # 4
print(third.counter)  # 0
print(Counter.counter, end='\n\n')  # 0

print('-' * 80, end='\n\n')


