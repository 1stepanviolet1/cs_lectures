# вызов метода через имя класса
# имя_класса.метод(экземпляр)

a = 10 # a - объект класса int
int.bit_length(a) # аналогично a.bit_length()

class Student:
    def __init__(self):
        self.name = 'Fedor'

    def print_hello(self):
        print('hello,', self.name)


st = Student()
st.print_hello()
Student.print_hello(st)




