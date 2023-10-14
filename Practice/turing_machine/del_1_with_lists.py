alphabet = [' ', 1]
memory = list(input())


def main():
    global memory
    print('memory:', memory)
    state = 'q0'
    i = 0
    while state != 'q2':
        if state == 'q0':
            memory, i, state = q0(memory, i)
        if state == 'q1':
            memory, i, state = q1(memory, i)
    print('result:', memory)


def q0(memory, index):
    if memory[index] == ' ':
        return memory, index + 1, 'q0'
    if memory[index] == '1':
        memory[index] = ' '
        return memory, index + 1, 'q1'


def q1(memory, index):
    if memory[index] == ' ':
        return memory, index, 'q2'
    if memory[index] == '1':
        memory[index] = ' '
        return memory, index + 1, 'q1'


if __name__ == '__main__':
    main()
