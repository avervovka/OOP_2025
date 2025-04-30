class Person:
    pass

person_1 = Person()
person_1.__dict__ = {'name': 'Vasya', 'age': '20', 'work': 'driver'}

# ваш код ниже:
for value in person_1.__dict__.values():
    print(value)
