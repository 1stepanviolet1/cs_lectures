countries = {"Russia": "Moscow", "Finland": "Helsinki", "USA": "New York", "USA": "Washington, D.C."} # ключи словаря уникальны
print('-' * 80, end='\n\n')
print('countries = {"Russia": "Moscow", "Finland": "Helsinki", "USA": "New York", "USA": "Washington, D.C."}, countries:', countries)
print('Цикл for по словарю countries:')
for country in countries:
    print(country)
countries["Japan"] = "Tokyo"
countries.update({'Canada':'Vancouver', 'Tanzania':'Dodoma'})
print('countries["Japan"] = "Tokyo", countries:', countries)
print('countries.pop("Japan"):', countries.pop("Japan"))
print('countries.popitem():', countries.popitem()) # неизвестно, какой именно элемент будет удален, поскольку элементы словаря неупорядочены
print('len(countries):', len(countries), end='\n\n')

print('-' * 80, end='\n\n')

print('Получить список ключей словаря:')
print(list(countries))
print(list(countries.keys()))
print("Получить список значений словаря:")
print(list(countries.values()))
print("Получить список пар: ключ, значение:")
print(list(countries.items()), end='\n\n')

print('-' * 80, end='\n\n')

print('Следующие операции приведут к ошибкам, чтобы увидеть ошибку, раскомментируйте строку кода:')
# print('{"a":"b"} < {"b":"c"}', {"a":"b"} < {"b":"c"})
# print('{"a":"b"} > {"b":"c"}', {"a":"b"} > {"b":"c"})
# print('{"a":"b"} + {"b":"c"}', {"a":"b"} + {"b":"c"})
# print('{"a":"b"} * 3', {"a":"b"} * 3)