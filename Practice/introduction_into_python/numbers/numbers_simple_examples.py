from pretty_print import block, get_strong_style


@block
def types_of_numbers():
    print(get_strong_style('Тип числа с плавающей точкой'.center(60)))
    print('type(3.4):'.center(30), '|', str(type(3.4)).center(25), end='\n\n')
    print(get_strong_style('Тип целого числа'.center(60)))
    print('type(3):'.center(30), '|', str(type(3)).center(25), end='\n\n')
    print(get_strong_style('Тип комплексного числа'.center(60)))
    print('type(3 + 6j):'.center(30), '|', str(type(3 + 6j)).center(25))


@block
def is_integer_examples():
    a = 3.4
    print(get_strong_style('Проверка на наличие дробной части у числа с плавающей точкой'.center(60)))
    print('a = 3.4, a.is_integer():'.center(30), '|', str(a.is_integer()).center(10))
    a = 3.0
    print('a = 3.0, a.is_integer():'.center(30), '|', str(a.is_integer()).center(10))


@block
def representation_of_the_number_in_computer_memory():
    print(get_strong_style('Примеры представления числа с плавающей точкой в памяти компьютера'.center(60)))
    print('0.1 + 0.2: '.center(30), '|', str(0.1 + 0.2).center(25))
    print('0.1 + 0.2 - 0.3:'.center(30), '|', str(0.1 + 0.2 - 0.3).center(25))
    print('0.1 + ... + 0.1 (8 раз):'.center(30), '|', str(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1).center(25))


if __name__ == '__main__':
    types_of_numbers()
    is_integer_examples()
    representation_of_the_number_in_computer_memory()
