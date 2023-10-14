from pretty_print import block, get_strong_style


@block
def creating_new_string_examples():
    print(get_strong_style("Метод format(<аргументы>) позволяет создать новую строку, подставляя в скобки {} аргументы по порядку".center(110)))
    print("'{} + {} = {}'.format(1, 2, 3)".center(55), '|', '{} + {} = {}'.format(1, 2, 3).center(55), end='\n\n')
    print(get_strong_style("Метод replace(arg1, arg2) создает новую строку, путем замены всех вхождений подстроки arg1 на arg2".center(110)))
    print("'AbAcDAb'.replace('Ab', '**')".center(55), '|', 'AbAcDAb'.replace('Ab', '**').center(55), end='\n\n')
    print(get_strong_style("Метод strip() удаляет все пробельные символы в начале и конце строки".center(110)))
    print("'\\n  abc abc abc \\n\\t'.strip()".center(55), '|', '\n  abc abc abc \n\t'.strip().center(55), end='\n\n')
    a = ['a', 'b', 'c', 'd']
    print(get_strong_style("Метод join(iter_obj) создает новую строку, конкатенируя элементы iter_obj и объект, у которого был вызван метод join()".center(110)))
    print(get_strong_style("Пример для случая, когда iter_obj - список".center(110)))
    print("a = ['a', 'b', 'c', 'd'], '_'.join(a)".center(55), '|', '_'.join(a).center(55))
    a = '1a2b3c4d5e6'
    print(get_strong_style("Пример для случая, когда iter_obj - строка".center(110)))
    print("a = '1a2b3c4d5e6', '_'.join(a)".center(55), '|', '_'.join(a).center(55))
    a = {"a.a":1, "b.b":2, "c.c":3}
    print(get_strong_style("Пример для случая, когда iter_obj - словарь (в конкатенации участвуют только ключи)".center(110)))
    print('a = {"a.a":1, "b.b":2, "c.c":3}, "_".join(a)'.center(55), '|', '_'.join(a).center(55), end='\n\n')


@block
def creating_list_from_string():
    a = '1_2_3_4_5_6'
    print(get_strong_style("Метод split(delimeter) создает список, разделяя объект строки, у которого был вызван метод split(), по строке delimeter".center(110)))
    print("a = '1_2_3_4_5_6', a.split('_')".center(55), '|', str(a.split('_')).center(55), end='\n\n')
    print(get_strong_style("Если не передавать аргумент в метод split(), качестве разделителя будут использоваться все пробельные символы".center(110)))
    a = 'a \n\tb   c   \nd\n\n'
    print("a = 'a \\n\\tb   c   \\nd\\n\\n', a.split()".center(55), '|', str(a.split()).center(55), end='\n\n')


@block
def codes_examples():
    print(get_strong_style("Получить код символа".center(110)))
    print("ord('Щ')".center(55), '|', str(ord('Щ')).center(55), end='\n\n')
    print(get_strong_style("Получить символ по его коду".center(110)))
    print("chr(15500)".center(55), '|', chr(15500).center(55), end='\n\n')


@block
def get_information_about_string():
    a = 'AbCdEf'
    print(get_strong_style("Метод find(substr) позволяет найти индекс подстроки substr в строке, у которой был вызван метод".center(110)))
    print("{}.find('E')".format(a).center(55), '|', str(a.find('E')).center(55))
    print("{}.find('e')".format(a).center(55), '|', str(a.find('e')).center(55), end='\n\n')
    print(get_strong_style("Метод isdigit() возвращает True, если строка состот из цифр и False в противном случае".center(110)))

    print("'Abc'.isdigit()".center(55), '|', str('Abc'.isdigit()).center(55))
    print("'-123'.isdigit()".center(55), '|', str('-123'.isdigit()).center(55))
    print("'-12.3'.isdigit()".center(55), '|', str('-12.3'.isdigit()).center(55))
    print("'123'.isdigit()".center(55), '|', str('123'.isdigit()).center(55), end='\n\n')



if __name__ == '__main__':
    creating_new_string_examples()
    creating_list_from_string()
    codes_examples()
    get_information_about_string()