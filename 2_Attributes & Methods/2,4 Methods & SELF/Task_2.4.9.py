class Simpsons:
    name = 'Simpsons'
    # здесь будет ваш метод
    def hi(self):
        return f'Привет, {self.name}'

bart = Simpsons()
lisa = Simpsons()
homer = Simpsons()

bart.name = 'Bart'
lisa.name = 'Lisa'
homer.name = 'Homer'

# здесь будет ваш код вызова метода:
print(bart.hi())
print(lisa.hi())
print(homer.hi())
