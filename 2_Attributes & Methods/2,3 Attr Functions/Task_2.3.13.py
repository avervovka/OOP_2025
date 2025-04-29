names = ['Klementina', 'Roza', 'Balu', 'Lena', 'Leonid']  # список имён

class Person:
    Vasya = ''
    Masha = ''
    Lena = ''
    Leonid = ''

# ниже ваш код:
for i in names:
    if hasattr(Person, i):
        delattr(Person, i)


# строки ниже не удаляйте, ради вселенной:
print(len(Person.__dict__))
