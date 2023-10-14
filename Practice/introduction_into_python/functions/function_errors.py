
magic_sum(a, b) # NameError: name 'magic_sum' is not defined: вызов функции раньше её определения


def magic_sum(a, b, c, d):
    return a + b+c+d


def magic_sum_with_error(a=10, b=10, c): # SyntaxError: non-default argument follows default argument: аргумент со значением по умолчанию идет раньше аргумента без 
    pass


print(magic_sum()) # TypeError: magic_sum() missing 2 required positional arguments: 'a' and 'b': функция вызвана без обязательных аргументов

magic_sum('a', 12) # TypeError: must be str, not int: вызов функции, в которой складываются строка и число

print(a) # NameError: name 'a' is not defined: переменная a видна только в функции

print(magic_sum(a = 1, 3)) # SyntaxError: positional argument follows keyword argument: сначала идет именованный, затем позиционный аргумент

