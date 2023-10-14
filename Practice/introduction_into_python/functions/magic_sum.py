def simple_magic_sum(a, b):
    sum = a + b
    return sum


print('-'*80, end='\n\n')
print("simple_magic_sum(1, 2):", simple_magic_sum(1, 2))
print("simple_magic_sum(3.4, 0.2):", simple_magic_sum(3.4, 0.2))
print("simple_magic_sum(1+7j, 2+4.5j):", simple_magic_sum(1+7j, 2+4.5j))
print("simple_magic_sum('1', '2'):", simple_magic_sum('1', '2'))
print("simple_magic_sum([1], ['2']):", simple_magic_sum([1], ['2']), end='\n\n')
print('-'*80, end='\n\n')


def magic_sum(a, b, p=10):
    return (a + b) * p


print('magic_sum(1, 3, 3):', magic_sum(1, 3, 3))
print('magic_sum(1, 3):', magic_sum(1, 3))
print('magic_sum(a=1, b=3, p=111):', magic_sum(a=1, b=3, p=111))
print('magic_sum(a=1, p=111, b=3):', magic_sum(a=1, p=111, b=3))
print('magic_sum(a=1, b=3):', magic_sum(1, b=3))
x = 9
y = 10
print('x = 9, y = 10, magic_sum(x, y):', magic_sum(x, y))
print('x = 9, magic_sum(x, x, x):', magic_sum(x, x, x), end='\n\n')
print('-'*80, end='\n\n')

print("magic_sum('a', '2'):", magic_sum('a', '2'))
print("magic_sum([1, 'kw'], ['201', 'r'], 5):", magic_sum([1, 'kw'], ['201', 'r'], 5), end='\n\n')
print('-'*80, end='\n\n')
print("magic_sum(magic_sum('1', '1'), magic_sum('1', '1'), magic_sum(1, 1, 1)):", magic_sum(magic_sum('1', '1'), magic_sum('1', '1'), magic_sum(1, 1, 1)), end='\n\n')
print('-'*80, end='\n\n')