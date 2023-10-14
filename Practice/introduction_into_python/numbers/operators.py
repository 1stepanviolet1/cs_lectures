from pretty_print import block, get_strong_style


@block
def operations_on_integers_and_real_numbers():
    print(get_strong_style('Возведение в степень'.center(40)))
    print(get_strong_style('Сначала 3 ** 2, затем 2 ** 9'.center(40)))
    print('2 ** 3 ** 2:'.center(20), '|', str(2 ** 3 ** 2).center(20), end='\n\n')
    print(get_strong_style('Нахождение остатка от деления'.center(40)))
    print('10 % 4:'.center(20), '|', str(10 % 4).center(20))


@block
def types():
    print(get_strong_style('Типы выражений'.center(40)))
    print('type(5 // 2):'.center(20), '|', str(type(5 // 2)).center(20))
    print('5 // 2:'.center(20), '|', str(5 // 2).center(20))
    print('type(5 // 2):'.center(20), '|', str(type(5 // 2)).center(20))
    print('5 / 2:'.center(20), '|', str(5 / 2).center(20))
    print('type(5 // 2):'.center(20), '|', str(type(5 // 2)).center(20))
    print('4 / 2:'.center(20), '|', str(4 / 2).center(20))


@block
def logical_operators():
    print(get_strong_style('Логические операторы'.center(40)))
    print('10 or 0:'.center(20), '|', str(10 or 0).center(20))
    print('10 and 0:'.center(20), '|', str(10 and 0).center(20))
    print('10 and not 0:'.center(20), '|', str(10 and not 0).center(20), end='\n\n')
    print(get_strong_style('Вычисление логических выражений ленивое'.center(40)))
    print('0 and False:'.center(20), '|', str(0 and False).center(20))
    print('0 or True:'.center(20), '|', str(0 or True).center(20))


@block
def comparison_operators():
    print(get_strong_style('Сравнение чисел'.center(40)))
    print(get_strong_style('То же самое, что 3 < 5 and 5 < 10'.center(40)))
    print('3 < 5 < 10:'.center(20), '|', str(3 < 5 < 10).center(20), end='\n\n')
    print(get_strong_style('То же самое, что 3 < 5 and 5 != 10'.center(40)))
    print('3 < 5 != 10:'.center(20), '|', str(3 < 5 != 10).center(20), end='\n\n')


if __name__ == '__main__':
    operations_on_integers_and_real_numbers()
    types()
    logical_operators()
    comparison_operators()

