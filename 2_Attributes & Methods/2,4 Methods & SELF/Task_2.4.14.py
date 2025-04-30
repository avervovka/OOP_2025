from itertools import count


class NewJournal:
    def set_attr(self, *args):
        self.count_money = sum([*args])

    def check_money(self):
        print(['Ура, денег хватает!', 'Денег не хватает'][self.count_money < 80])

masha = NewJournal()
masha.set_attr(10, 20, 30, 40)
masha.check_money()
