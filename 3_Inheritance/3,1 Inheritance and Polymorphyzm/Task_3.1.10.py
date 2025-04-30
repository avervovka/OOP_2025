class Kondraty_Palich:
    status = 'Деда'

class Vasya(Kondraty_Palich):
    status = 'Отец'

class Masha(Vasya):
    status = 'Дочь'

# подумайте что можно поменять вот здесь:
masha = Masha()
vasya = Vasya()

# эту часть кода не исправляйте:
print(masha.status, vasya.status, sep='\n')
