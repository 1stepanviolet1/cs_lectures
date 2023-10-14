a = 1
b = 1

print('-' * 80, end='\n\n')
print(' a = 1, NOT a: ~a =', ~a, end='\n\n')
print(' a = (0)01')  # Бесконечное количество нулей, потому что число неограниченной точности
print('~a = (1)10', end='\n\n')  # Бесконечное количество единиц, потому что инвертируется бесконечное количество нулей
print('-' * 80, end='\n\n')
print(' a = (0)01')
print(' b = (0)01', end='\n\n')
print(' a = 1, b = 1, a AND b: a & b =', a & b, end='\n\n')
print('-' * 80, end='\n\n')
b = 0
print(' a = (0)01')
print(' b = (0)00', end='\n\n')
print(' a = 1, b = 0, a AND b: a & b =', a & b, end='\n\n')
print('-' * 80, end='\n\n')
b = 2
print(' a = (0)01')
print(' b = (0)10', end='\n\n')
print(' a = 1, b = 2, a AND b: a & b =', a & b, end='\n\n')
print('-' * 80, end='\n\n')
b = 3
print(' a = (0)01')
print(' b = (0)11', end='\n\n')
print(' a = 1, b = 3, a AND b: a & b =', a & b, end='\n\n')
print('-' * 80, end='\n\n')

b = 1
print(' a = (0)01')
print(' b = (0)01', end='\n\n')
print(' a = 1, b = 1, a OR b: a | b =', a | b, end='\n\n')
print('-' * 80, end='\n\n')
b = 0
print(' a = (0)01')
print(' b = (0)00', end='\n\n')
print(' a = 1, b = 0, a OR b: a | b =', a | b, end='\n\n')
print('-' * 80, end='\n\n')
b = 2
print(' a = (0)01')
print(' b = (0)10', end='\n\n')
print(' a = 1, b = 2, a OR b: a | b =', a | b, end='\n\n')
print('-' * 80, end='\n\n')
b = 3
print(' a = (0)01')
print(' b = (0)11', end='\n\n')
print(' a = 1, b = 3, a OR b: a | b =', a | b, end='\n\n')
print('-' * 80, end='\n\n')

b = 1
print(' a = (0)01')
print(' b = (0)01', end='\n\n')
print(' a = 1, b = 1, a XOR b: a ^ b =', a ^ b, end='\n\n')
print('-' * 80, end='\n\n')
b = 0
print(' a = (0)01')
print(' b = (0)00', end='\n\n')
print(' a = 1, b = 0, a XOR b: a ^ b =', a ^ b, end='\n\n')
print('-' * 80, end='\n\n')
b = 2
print(' a = (0)01')
print(' b = (0)10', end='\n\n')
print(' a = 1, b = 2, a XOR b: a ^ b =', a ^ b, end='\n\n')
print('-' * 80, end='\n\n')
b = 3
print(' a = (0)01')
print(' b = (0)11', end='\n\n')
print(' a = 1, b = 3, a XOR b: a ^ b =', a ^ b, end='\n\n')
print('-' * 80, end='\n\n')

a = 10
print('a = (0)1010')
print('a = 10. Узнать последний бит числа a: a & 1:', a & 1)
print('a = 10. Сдвинуть число a на 1 бит вправо: a >> 1:', a >> 1)
print('a = 10. Сдвинуть число a на 1 бит влево: a << 1:', a << 1)
