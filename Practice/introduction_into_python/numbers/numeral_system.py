from pretty_print import block, get_strong_style


@block
def bin_numbers():
    a = 0b1101
    print(get_strong_style('Перевод из двоичной в десятичную'.center(50)))
    print('a = 0b1101:'.center(25), '|', str(a).center(25), end='\n\n')
    print(get_strong_style('Перевод из десятичной в двоичную'.center(50)))
    print('bin(99):'.center(25), '|', str(bin(99).center(25)))


@block
def oct_numbers():
    a = 0o1111
    print(get_strong_style('Перевод из восьмеричной в десятичную'.center(50)))
    print('a = 0o1111:'.center(25), '|', str(a).center(25), end='\n\n')
    print(get_strong_style('Перевод из десятичной в восьмеричную'.center(50)))
    print('oct(99):'.center(25), '|', str(oct(99).center(25)))


@block
def hex_numbers():
    a = 0xA67
    print(get_strong_style('Перевод из шестнадцатиричной в десятичную'.center(50)))
    print('a = 0xA67:'.center(25), '|', str(a).center(25), end='\n\n')
    print(get_strong_style('Перевод из десятичной в шестнадцатиричную'.center(50)))
    print('hex(99):'.center(25), '|', str(hex(99).center(25)))


@block
def int_function_examples_in_numeral_system():
    print(get_strong_style('Использование функции int() при работе с системами счисления'.center(50)), end='\n\n')
    print(get_strong_style('Первый аргумент: строка, которая может быть преобразована в число'.center(50)))
    print(get_strong_style('Второй аргумент: основание системы счисления, '
                           'из которой число будет переведено в десятичную систему счисления'.center(50)))
    print("int('100', base=2):".center(25), '|', str(int('100', base=2)).center(25))
    print("int('200', base=3):".center(25), '|', str(int('200', base=3)).center(25))
    print("int('600', base=7):".center(25), '|', str(int('600', base=7)).center(25))
    print("int('A1B2', base=12):".center(25), '|', str(int('A1B2', base=12)).center(25), end='\n\n')
    print(get_strong_style('По умолчанию второй аргумент равен 10'.center(50)))
    print("int('100'):".center(25), '|', str(int('100')).center(25))


if __name__ == '__main__':
    bin_numbers()
    oct_numbers()
    hex_numbers()
    int_function_examples_in_numeral_system()
