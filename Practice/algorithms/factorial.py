def fact_iter(a):
    if a == 1:
        return 1
    res = a
    for i in range(2, a):
        res *= i
    return res


def fact_rec(a):
    if a == 1:
        return 1
    return a * fact_rec(a-1)


x = int(input())
print('fact iter:', fact_iter(x))
print('fact rec:', fact_rec(x)) # для числа 999 будет превышено максимальное количество рекурсивных вызовов