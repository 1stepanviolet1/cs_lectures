import math
import cmath
from pretty_print import block, get_strong_style


@block
def print_math_examples():
    X = 12
    print(get_strong_style('Нахождение факториала'.center(60)))
    print('math.factorial(12):'.center(30), '|', str(math.factorial(X)).center(30), end='\n\n')
    print(get_strong_style('Нахождение квадратного корня'.center(60)))
    print('math.sqrt(12):'.center(30), '|', str(math.sqrt(X)).center(30), end='\n\n')
    print(get_strong_style('Число Пи'.center(60)))
    print('math.pi'.center(30), '|', str(math.pi).center(30), end='\n\n')
    print(get_strong_style('Экспонента'.center(60)))
    print('math.e'.center(30), '|', str(math.e).center(30))


@block
def print_cmath_examples():
    X = -12
    print(get_strong_style('Нахождение квадратного корня из отрицательного числа'.center(60)))
    print('cmath.sqrt(-12)'.center(30), '|', str(cmath.sqrt(X)).center(30), end='\n\n')
    print(get_strong_style('Комплексно сопряженное число'.center(60)))
    print('cmath.sqrt(-12).conjugate():'.center(30), '|', str(cmath.sqrt(X).conjugate()).center(30), end='\n\n')
    print(get_strong_style('Мнимая часть (Число с плавающей точкой)'.center(60)))
    print('cmath.sqrt(-12).imag:'.center(30), '|', str(cmath.sqrt(X).imag).center(30), end='\n\n')
    print(get_strong_style('Действительная часть (число с плавающей точкой)'.center(60)))
    print('cmath.sqrt(-12).real:'.center(30), '|', str(cmath.sqrt(X).real).center(30))


if __name__ == '__main__':
    print_math_examples()
    print_cmath_examples()