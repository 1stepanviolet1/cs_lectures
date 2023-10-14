# поля класса доступны через имя класса и одинаковы для всех экземпляров, которые не переопределили его

class Student:
    marks = []  # поле класса, изменяемый объект

    def __init__(self, name):
        self.name = name

    def add_mark(self, x):
        Student.marks.append(x) # доступ через имя класса

    def add_mark_with_self(self, x):
        self.marks.append(x) # доступ через экземпляр


Maria = Student('Maria')
Oleg = Student('Oleg')

Maria.add_mark(4)  # поле marks изменилось для всех экземпляров и для класса Student, мы меняем объект
print(Maria.marks)  # [4]
print(Oleg.marks)  # [4]
print(Student.marks)  # [4]

Maria.marks = [2, 3, 5] # поле marks переопределено для экземпляра Maria, мы не меняем объект, мы присваиваем новый список
print(Maria.marks)  # [2, 3, 5]
print(Oleg.marks)  # [4]
print(Student.marks)  # [4]

Maria.add_mark(4)  # поле marks изменилось для всех, кроме Maria, поскольку меняется поле у класса
print(Maria.marks)  # [2, 3, 5]
print(Oleg.marks)  # [4, 4]
print(Student.marks)  # [4, 4]

Maria.add_mark_with_self(4)  # поле marks изменилось для Maria, поскольку меняется поле у экземпляра
print(Maria.marks)  # [2, 3, 5, 4]
print(Oleg.marks)  # [4, 4]
print(Student.marks)  # [4, 4]