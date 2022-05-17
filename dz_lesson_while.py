from re import T


user_name1 = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

while True:
    name1 = list.pop(user_name1)
    if name1 == 'Валера':
        break

print(f'{name1} нашелся.')



user_name2 = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_personal(name2):
    while True:
        if name2 in user_name2:
            print (f'{name2} нашелся.')
            break
        else:
            print (f'{name2} не нашелся.')
            return

find_personal(name2=input('Введите имя: '))



def ask_user():
    while True:
        user_say = input('Как дела? ')
        if user_say == 'Хорошо':
            break
            return

ask_user()



def get_answer():
    while True:
        user_answer = input('Задайте Ваш вопрос: ')
        if user_answer.lower() == 'как дела?':
            print('Всё в порядке!')
        elif user_answer != 'Пока!':
            print('Не хочу отвечать на этот вопрос!')
        else:
            break
            return

get_answer()