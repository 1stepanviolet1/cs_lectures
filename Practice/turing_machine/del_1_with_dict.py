def main():
    global memory
    print('memory:', memory)
    state = 'q0'
    i = 0
    while state != 'q2':
        symbol, direction, state = table[state][memory[i]]
        memory[i] = symbol
        i += direction
    print('result', memory)
    memory = '1'
    print(memory)


if __name__ == '__main__':
    memory = list(input())
    table = {'q0': {' ': [' ', 1, 'q0'], '1': [' ', 1, 'q1']},
             'q1': {' ': [' ', 0, 'q2'], '1': [' ', 1, 'q1']}}
    main()
    print(memory)
