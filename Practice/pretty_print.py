def block(func):
    def wrapper():
        print('-' * 80, end='\n\n')
        func()
        print()
    return wrapper


def get_strong_style(string):
    return '\x1b[1;m{}\x1b[0m'.format(string)
