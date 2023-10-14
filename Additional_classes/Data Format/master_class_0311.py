# Получение обратного кода

n = 8
print('Мы работаем в {}-ми разрядной архитектуре'.format(n))
num = int(input('Введите целое число (в 10 СС): '))
print('Вы ввели числов в 10-СС: {}'.format(num))
bit_len = num.bit_length()
bin_str = "{:b}".format(abs(num))
print('Число в 2-СС: {}{}'.format('-' * int(num < 0), bin_str))
print('Длина бин. представления: {}'.format(bit_len))
delta = n - bit_len
code_1_str = bin_str.zfill(8)
mask_inv = 2 ** bit_len - 1  # макса для инверсии
mask_str = '{:b}'.format(mask_inv).zfill(8)
print('Маска для инверсии: {}'.format(mask_inv))

inv_num = abs(num) ^ mask_inv  # применили маску для инверсии
inv_str = '{:b}'.format(inv_num).zfill(8)
print('Результат инверсии: {}'.format(inv_num))

code_1_num = int(code_1_str, 2)

if num < 0:
    mask_negative = 2 ** (n - 1)
    code_1_num = code_1_num | mask_negative
    inv_num = inv_num | mask_negative

print('Число в прямом коде (в 2-СС): {:b}'.format(code_1_num))
print('Маска для инверсии (в 2-СС) : {}'.format(mask_str))
print('Обратный код числа (в 2-CC) : {:b}'.format(inv_num))

# TODO: вывод результата для положительного числа с незначащими нулями


# '00001100'
# ^
# '11111111'
#  11110011
# '11110011'