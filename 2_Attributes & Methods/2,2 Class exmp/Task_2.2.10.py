# Напишите ваш код:
class Holiday:
    pass

friends = Holiday()
friends.__dict__ = dict(zip((f'name{i}' for i in range(1, 6)), 'Sveta Katya Lena Natasha The_Horse_in_the_coat'.split()))


# Код ниже пожалуйста не удаляйте, ради Машеньки!
for i in friends.__dict__:
    if i != 'name5':
        print(getattr(friends, i))
    elif i == 'name5' and getattr(friends, i) == 'Leonardo DiCaprio':
        raise AttributeError('Машенька хочет увидеть вас на ДР')


