class BirthDay:
    def __init__(self, present, color):
        self.present = present
        self.color = color


masha = BirthDay("pen", "red")
nikita = BirthDay("t-shirt", "red")
lena = BirthDay("ball", "red")
names_russian = ["Маша", "Никита", "Лена"]
names = [masha, nikita, lena]
counter = 0
for name in names_russian:
    word = 'подарил'
    if name != 'Никита':
        word += 'а'
    print(f'{name} {word}: {names[counter].present}, цвета: {names[counter].color}')
    counter += 1
