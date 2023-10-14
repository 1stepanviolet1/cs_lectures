def magic_sum(a, b):
    return a + b


magic_sum(1, 1) # Этот код исполнится при импорте

print(__name__) # При импорте модуля functions __name__ равно 'functions', при исполнении python3 functions.py __name__ равно '__main__'


if __name__ == '__main__':
    magic_sum(2, 2)  # Этот код не исполнится при импорте