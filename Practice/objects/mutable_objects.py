def change_list(x):
    x += ['World!']
    print('Список x в функции change_list(x):', x, end='\n\n')


print('-' * 80, end='\n\n')
x = ['Hello, ']
print('Список x до функции change_list(x):', x, end='\n\n')
change_list(x)
print('Список x после функции change_list(x):', x, end='\n\n')
print('Список x изменился, поскольку списки изменяемые.')
print('-'*80, end='\n\n')