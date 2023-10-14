countries_list = ['Russia', 'Germany', 'Great Britain']

countries_dict = {'Russia':'Russian', 'Great Britain': 'English', 'France':'French'}

print('-'*80)
print('Первый вариант решения задачи:')
print('-' * 80, end='\n\n')

for country in countries_list:
    if country in countries_dict:
        print(countries_dict[country])
    else:
        print('unknown country')
print()
print('-' * 80)
print('Второй вариант решения задачи:')
print('-' * 80, end='\n\n')

for country in countries_list:
    print(countries_dict.get(country, 'unknown country'))
