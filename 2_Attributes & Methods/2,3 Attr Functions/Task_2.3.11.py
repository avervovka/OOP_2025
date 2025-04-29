pok = ['pikachu', 'scyther', 'gyarados', 'gengar']
pok_proverka = ['lapras', 'pikachu', 'alakazam']

class Pokemon:
    pass


pokemons = Pokemon()
for i in pok:
    setattr(pokemons, i, '')


for i in pok_proverka:
    print(hasattr(pokemons, i))
