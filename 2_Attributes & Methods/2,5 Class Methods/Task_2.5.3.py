class UZ:

    @classmethod
    def mult(cls, x, y):
        cls.x = x
        cls.y = y
        print(cls.x * cls.y)


UZ.mult(20, 5)
