def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый получит {parts} пирога')
    except ZeroDivisionError:
        print('Не надо делить на 0!')
    except TypeError:
        print('Программа принимает число')


cut_cake(0)
cut_cake('4')

# Какие бывают исключения?
# Базовые - Exception , BaseException
# Исключения ОС - ConnectionError , TimeoutError и т.д.
# # Основные - ValueError , TypeError , IndexError , KeyError и т.д.
# https://docs.python.org/3.5/library/exceptions.html