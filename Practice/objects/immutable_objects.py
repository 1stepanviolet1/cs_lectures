def change_string(x):
    x += 'World!'
    print('Строка x в функции change_list(x):', x, end='\n\n')


print('-' * 80, end='\n\n')
x = 'Hello, '
print('Строка x до функции change_list(x):', x, end='\n\n')
change_string(x)
print('Строка x после функции change_list(x):', x, end='\n\n')
print('Строка x не изменилась, поскольку строки неизменяемые.')
print('-'*80, end='\n\n')