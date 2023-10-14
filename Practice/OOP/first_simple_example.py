# Простейший класс, атрибуты экземпляра класса
# Конструктор, создание экземпляра класса


class Student:
    def __init__(self):  # конструктор; self - текущий экземпляр класса Student;  конструктор ничего не возвращает
        self.name = 'Fedor'  # атрибут экземпляра класса Student
        name = 'Petr' # локальная переменная в конструкторе


new_student = Student()  # создание экземпляра класса Student, вызывается метод __init__, self - new_student
print(new_student.name)  # Fedor
