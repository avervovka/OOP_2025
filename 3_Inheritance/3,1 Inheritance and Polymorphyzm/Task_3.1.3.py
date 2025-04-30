class Homer:
    def __init__(self, name):
        self.name = name

class Daughter(Homer):
    pass

daughter1 = Daughter('Lisa')
print(daughter1.name)
