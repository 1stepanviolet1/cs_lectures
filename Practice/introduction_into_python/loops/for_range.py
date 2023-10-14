my_list = list('abcdefg')
print('-'*80, end='\n\n')
print('Список:', my_list, end='\n\n')
print('-'*80, end='\n\n')

for el in my_list:
    print(el, end=' ')

print(end='\n\n')
print('-'*80, end='\n\n')

for i in range(len(my_list)):
    print(i, end=' ')

print(end='\n\n')
print('-'*80, end='\n\n')

for i, el in enumerate(my_list):
    print(i, el, end='; ')

print(end='\n\n')
print('-'*80, end='\n\n')