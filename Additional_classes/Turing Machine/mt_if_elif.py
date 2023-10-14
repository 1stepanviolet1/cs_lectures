memory = list(input())
q = 'q0'  # текущее состояние автомата
idx = 0  # чтобы посмотреть в ленту: memory[idx]; 1 ==> R, -1 ==> L, 0 ==> N

while q != 'qT':
    # если текущее состояние q0 и вижу на ленте 'a', тогда делаю
    if q == 'q0':
        if memory[idx] == 'a':  # <’b’, R, q1> делаю:
            memory[idx] = 'b'  # 1) пишу в клетку символ 'b',
            idx += 1  # 2) двигаюсь направо,
            q = 'q1'  # 3) перехожу в состояние q1 -- меняю текущее состояние на q1
        elif memory[idx] == 'b':  # <’b’, R, q1> делаю:
            memory[idx] = 'b'
            idx += 1
            q = 'q1'
        elif memory[idx] == ' ':  # else:
            memory[idx] = ' '
            idx += 1
            q = 'q0'
    elif q == 'q1':
        if memory[idx] == 'a':  # <’b’, R, q1> делаю:
            memory[idx] = 'b'  # 1) пишу в клетку символ 'b',
            idx += 1  # 2) двигаюсь направо,
            q = 'q1'  # 3) перехожу в состояние q1 -- меняю текущее состояние на q1
        elif memory[idx] == 'b':  # <’b’, R, q1> делаю:
            memory[idx] = 'b'
            idx += 1
            q = 'q1'
        elif memory[idx] == ' ':  # else:
            memory[idx] = ' '
            idx += 0
            q = 'qT'

print(''.join(memory))
