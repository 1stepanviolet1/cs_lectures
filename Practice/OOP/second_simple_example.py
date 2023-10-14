# Простейший класс, методы класса
# Конструктор с параметрами, создание экземпляра класса

class Student:
    def __init__(self, age, name='Fedor'):  # self - текущий экземпляр класса Student, name - аргумент по умолчанию
        self.name = name  # атрибут name экземпляра класса Student
        self.age = age # атрибут age экземпляра класса Student


    def print_hello(self): # метод класса Student
        print('hello,', self.name)


new_student_1 = Student(17)  # создание экземпляра класса Student, вызывается метод __init__, передается только age
print(new_student_1.name) # Fedor

new_student_2 = Student(20, 'Katya')  # создание экземпляра класса Student, вызывается метод __init__, передается age=20, name='Katya'
print(new_student_2.name) # Katya

new_student_1.print_hello() # вызов метода print_hello() для self = new_student_1
new_student_2.print_hello() # вызов метода print_hello() для self = new_student_2