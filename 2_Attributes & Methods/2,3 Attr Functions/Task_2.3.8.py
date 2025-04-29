list_person = ['hobby', 'work', 'study']

class Person:
    hobby = 'dance'
    work = 'design'
    study = 'college'

# ваш код ниже:
id_1 = Person()
for i in list_person:
    print(getattr(id_1, i))
