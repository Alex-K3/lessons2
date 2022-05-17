def hello_user():
    while True:
        try:
            user_say = input('Скажи что-нибудь: ')
            if user_say == 'Пока':
                print('Ну пока')
                break
            else:
                print('Сам ты {}'.format(user_say))
        except KeyboardInterrupt:
            print('Пока!')
            break
    
hello_user()


def discounted (price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise ValueError('Максимальная скидка не должна быть больше 100')
        elif discount >= max_discount:
            price_with_discount = price
        else:
            price_with_discount = price - (price * discount / 100)
        return price_with_discount
    except (ValueError, TypeError):
        print('Программа принимает число')

price_discounted = discounted('100', 50)
print(price_discounted)