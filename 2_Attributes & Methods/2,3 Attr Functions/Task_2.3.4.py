class Person:
    def __init__(self):
        self.name = None

    pass


id_1 = Person()
setattr(id_1, 'name','Vasya')
setattr(id_1, 'name', 'Masha')
print(id_1.name)

